from datetime import datetime

import os
import re
import time

import pandas as pd
import requests


# OPENALEX SLR TOOL
#
# Mục đích:
#   - Thu thập metadata bài báo từ OpenAlex
#   - Phục vụ bước V1 Retrieval của SLR
#   - Lấy toàn bộ kết quả mà OpenAlex trả về
#   - Deduplicate records
#   - Không thực hiện screening
#   - Không tự động quyết định INCLUDE / EXCLUDE
#
# Workflow:
#
#   OpenAlex
#       ↓
#   V1 Retrieval
#       ↓
#   Raw records
#       ↓
#   Deduplication
#       ↓
#   01_all_records.csv
#       ↓
#   V2 Screening bên ngoài tool này
#
# Output:
#
#   Pham Nhat Thang/
#       SLR/
#           01_all_records.csv
#           search-log.md
#
# Search String:
#
# SEARCH_QUERY = (
#    '("JUnit testing" OR "unit test augmentation" OR "IBM CodeNet" OR "Project_CodeNet_Java250") '
#    'AND (JaCoCo OR PITest OR "coverage-guided testing" OR "mutation-guided testing") '
#    'AND ("mutation score" OR "mutant detection" OR "mutation testing effectiveness")'
#)



# 1. CONFIGURATION

STUDENT_FOLDER = "Pham Nhat Thang"

OUTPUT_FOLDER = "SLR"

OPENALEX_API_KEY = os.getenv(
    "OPENALEX_API_KEY",
    None
)


# Search String V1

SEARCH_QUERY = (
    '("JUnit testing" OR "unit test augmentation" OR "IBM CodeNet" OR "Project_CodeNet_Java250") '
    'AND (JaCoCo OR PITest OR "coverage-guided testing" OR "mutation-guided testing") '
    'AND ("mutation score" OR "mutant detection" OR "mutation testing effectiveness")'
)

QUERY_ID = "OA-V1-01"


# Retrieval configuration


MAX_RECORDS = None


# Số record tối đa mỗi request
OPENALEX_PAGE_SIZE = 200


# Timeout mỗi HTTP request
REQUEST_TIMEOUT = 20


# Retry tối đa khi HTTP 429
MAX_RETRIES = 5


# Thời gian chờ ban đầu khi bị rate limit
RETRY_DELAY = 10


# 2. HELPER FUNCTIONS

def normalize_doi(doi):


    if doi is None:
        return ""

    doi = str(doi).strip()

    if doi.lower() == "nan":
        return ""

    doi = re.sub(
        r"^https?://doi\.org/",
        "",
        doi,
        flags=re.IGNORECASE
    )

    return doi.strip().lower()


def normalize_text(text):


    if pd.isna(text):
        return ""

    text = str(text).lower()

    text = re.sub(
        r"[^\w\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def normalize_authors(authors):


    if pd.isna(authors):
        return ""

    authors = str(authors).lower()

    authors = re.sub(
        r"[^\w\s;]",
        "",
        authors
    )

    authors = re.sub(
        r"\s+",
        " ",
        authors
    )

    return authors.strip()


def reconstruct_abstract(inverted_index):


    if not inverted_index:
        return ""

    positions = {}

    for word, indexes in inverted_index.items():

        for index in indexes:
            positions[index] = word

    if not positions:
        return ""

    return " ".join(
        positions[index]
        for index in sorted(positions)
    )


# 3. FETCH OPENALEX

def fetch_openalex(
    query,
    query_id,
    api_key=None,
    max_records=None
):


    url = "https://api.openalex.org/works"

    cursor = "*"

    raw_records = []

    retry_count = 0

    print()
    print("=" * 70)
    print("OPENALEX SEARCH")
    print("=" * 70)

    print(f"Query ID      : {query_id}")

    if max_records is None:
        print("Max records   : ALL")
    else:
        print(f"Max records   : {max_records}")

    print()

    print("Search string:")
    print(query)

    print("=" * 70)


    # Cursor pagination

    while cursor:

        # Xác định số record cần lấy trong page hiện tại

        if max_records is None:

            per_page = OPENALEX_PAGE_SIZE

        else:

            remaining = (
                max_records
                - len(raw_records)
            )

            if remaining <= 0:
                break

            per_page = min(
                OPENALEX_PAGE_SIZE,
                remaining
            )


        # Request parameters

        params = {
            "search": query,
            "per-page": per_page,
            "cursor": cursor
        }

        if api_key:
            params["api_key"] = api_key


        # HTTP request

        try:

            response = requests.get(
                url,
                params=params,
                timeout=REQUEST_TIMEOUT
            )


            # HTTP 429 - Rate limit

            if response.status_code == 429:

                retry_count += 1

                print(
                    f"[OpenAlex] HTTP 429 - "
                    f"rate limited "
                    f"({retry_count}/{MAX_RETRIES})"
                )

                if retry_count > MAX_RETRIES:

                    raise RuntimeError(
                        "OpenAlex rate limit 429 "
                        "quá số lần retry cho phép."
                    )

                time.sleep(
                    RETRY_DELAY
                )

                continue


            # Request thành công

            retry_count = 0

            response.raise_for_status()

            data = response.json()


            # Results

            results = data.get(
                "results",
                []
            )


            if not results:

                print(
                    "[OpenAlex] Không còn kết quả."
                )

                break


            raw_records.extend(
                results
            )


            # Progress

            if max_records is None:

                print(
                    f"[OpenAlex] Đã lấy "
                    f"{len(raw_records)} records"
                )

            else:

                print(
                    f"[OpenAlex] Đã lấy "
                    f"{len(raw_records)}/"
                    f"{max_records} records"
                )


            # Next cursor

            cursor = (
                data
                .get("meta", {})
                .get("next_cursor")
            )


            # Nếu có giới hạn và đã đủ record

            if (
                max_records is not None
                and len(raw_records) >= max_records
            ):
                break


        # Request error

        except requests.RequestException as e:

            print(
                f"[OpenAlex Request Error] {e}"
            )

            break


        # Unexpected error

        except Exception as e:

            print(
                f"[OpenAlex Error] {e}"
            )

            break


    # Chuẩn hóa dữ liệu

    records = []

    fetched_date = datetime.now().strftime(
        "%Y-%m-%d"
    )



    if max_records is None:

        selected_records = raw_records

    else:

        selected_records = raw_records[
            :max_records
        ]


    for work in selected_records:

        # Abstract

        abstract = reconstruct_abstract(
            work.get(
                "abstract_inverted_index"
            )
        )


        # DOI

        doi = normalize_doi(
            work.get("doi")
        )


        # Authors

        authors = []

        for authorship in work.get(
            "authorships",
            []
        ):

            author = (
                authorship.get("author")
                or {}
            )

            name = author.get(
                "display_name"
            )

            if name:
                authors.append(name)


        authors_text = "; ".join(
            authors
        )


        # Venue

        primary_location = (
            work.get(
                "primary_location"
            )
            or {}
        )

        source = (
            primary_location.get(
                "source"
            )
            or {}
        )

        venue = (
            source.get(
                "display_name"
            )
            or ""
        )


        # URL

        url = (
            work.get("doi")
            or work.get("id")
            or ""
        )


        # Open Access

        open_access = (
            work.get(
                "open_access"
            )
            or {}
        )

        is_open_access = bool(
            open_access.get(
                "is_oa",
                False
            )
        )


        # Citation count

        citation_count = work.get(
            "cited_by_count",
            0
        )


        # Record

        record = {

            # Core fields
            "source": "OpenAlex",

            "title": (
                work.get("title")
                or ""
            ),

            "authors": authors_text,

            "year": (
                work.get(
                    "publication_year"
                )
            ),

            "venue": venue,

            "doi": doi,

            "abstract": abstract,

            "url": url,

            "query": query,

            "fetched_date": fetched_date,


            # Additional metadata
            "query_id": query_id,

            "citation_count": citation_count,

            "is_open_access": is_open_access
        }


        records.append(
            record
        )


    print()

    print(
        f"[OpenAlex] Raw records: "
        f"{len(records)}"
    )

    return records


# 4. DEDUPLICATION

def deduplicate_records(df):
    """
    Deduplicate theo quy tắc:

    1. Có DOI
       -> dedup bằng DOI.

    2. Không có DOI
       -> dedup bằng:

          title + authors + year

    Không dùng abstract để dedup.
    """

    if df.empty:
        return df.copy()


    df = df.copy()


    # Chuẩn hóa DOI

    df["doi"] = (
        df["doi"]
        .fillna("")
        .apply(normalize_doi)
    )


    # Có DOI

    df_has_doi = (
        df[
            df["doi"] != ""
        ]
        .drop_duplicates(
            subset=["doi"],
            keep="first"
        )
        .copy()
    )


    # Không DOI

    df_no_doi = (
        df[
            df["doi"] == ""
        ]
        .copy()
    )


    if not df_no_doi.empty:

        df_no_doi[
            "title_clean"
        ] = (
            df_no_doi["title"]
            .apply(normalize_text)
        )


        df_no_doi[
            "authors_clean"
        ] = (
            df_no_doi["authors"]
            .apply(normalize_authors)
        )


        df_no_doi[
            "year_clean"
        ] = (
            df_no_doi["year"]
            .fillna("")
            .astype(str)
        )


        df_no_doi[
            "dedup_key"
        ] = (
            df_no_doi["title_clean"]
            + "|"
            + df_no_doi["authors_clean"]
            + "|"
            + df_no_doi["year_clean"]
        )


        df_no_doi = (
            df_no_doi
            .drop_duplicates(
                subset=["dedup_key"],
                keep="first"
            )
            .copy()
        )


        df_no_doi.drop(
            columns=[
                "title_clean",
                "authors_clean",
                "year_clean",
                "dedup_key"
            ],
            inplace=True
        )


    # Merge

    df_result = pd.concat(
        [
            df_has_doi,
            df_no_doi
        ],
        ignore_index=True
    )


    return df_result


# 5. SEARCH LOG

def initialize_search_log(log_path):


    if os.path.exists(
        log_path
    ):
        return


    with open(
        log_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "# Search Log\n\n"
        )

        file.write(
            "| Date | Database | Query ID | "
            "Query | Raw Records | "
            "After Dedup | Note |\n"
        )

        file.write(
            "|---|---|---|---|---:|---:|---|\n"
        )


def append_search_log(
    log_path,
    database,
    query_id,
    query,
    raw_count,
    dedup_count,
    note=""
):


    initialize_search_log(
        log_path
    )


    date = datetime.now().strftime(
        "%Y-%m-%d"
    )


    safe_query = (
        query
        .replace("|", "\\|")
        .replace("\n", " ")
        .strip()
    )


    with open(
        log_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"| {date} | "
            f"{database} | "
            f"{query_id} | "
            f"`{safe_query}` | "
            f"{raw_count} | "
            f"{dedup_count} | "
            f"{note} |\n"
        )


def append_total_log(
    log_path,
    raw_count,
    dedup_count
):


    date = datetime.now().strftime(
        "%Y-%m-%d"
    )


    with open(
        log_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"| **{date}** | "
            f"**TỔNG CỘNG** | "
            f"**V1 Retrieval** | "
            f"**Tất cả các nguồn** | "
            f"**{raw_count}** | "
            f"**{dedup_count}** | "
            f"**Current run** |\n"
        )


# 6. EXPORT CSV

def export_records(
    df,
    output_path
):


    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )


# 7. MAIN OPENALEX PIPELINE

def run_openalex_pipeline():

    print()

    print("#" * 70)
    print("# OPENALEX SLR DATA COLLECTION TOOL")
    print("#" * 70)


    # Output directory

    output_dir = os.path.join(
        STUDENT_FOLDER,
        OUTPUT_FOLDER
    )


    os.makedirs(
        output_dir,
        exist_ok=True
    )


    csv_path = os.path.join(
        output_dir,
        "01_all_records.csv"
    )


    log_path = os.path.join(
        output_dir,
        "search-log.md"
    )


    # 1. FETCH

    print()

    print("[1/5] FETCH OPENALEX")


    records = fetch_openalex(
        query=SEARCH_QUERY,
        query_id=QUERY_ID,
        api_key=OPENALEX_API_KEY,
        max_records=MAX_RECORDS
    )


    if not records:

        print()

        print(
            "[STOP] OpenAlex không trả về record."
        )

        return


    raw_count = len(
        records
    )


    # 2. DATAFRAME

    print()

    print(
        "[2/5] CREATE DATAFRAME"
    )


    df_raw = pd.DataFrame(
        records
    )


    # 3. DEDUP

    print()

    print(
        "[3/5] DEDUPLICATION"
    )


    df_dedup = deduplicate_records(
        df_raw
    )


    dedup_count = len(
        df_dedup
    )


    print(
        f"Raw records : {raw_count}"
    )


    print(
        f"After dedup : {dedup_count}"
    )


    print(
        f"Removed     : "
        f"{raw_count - dedup_count}"
    )


    # 4. EXPORT

    print()

    print(
        "[4/5] EXPORT CSV"
    )


    export_records(
        df=df_dedup,
        output_path=csv_path
    )


    print(
        f"Saved: {csv_path}"
    )


    # 5. SEARCH LOG

    print()

    print(
        "[5/5] UPDATE SEARCH LOG"
    )


    append_search_log(
        log_path=log_path,
        database="OpenAlex",
        query_id=QUERY_ID,
        query=SEARCH_QUERY,
        raw_count=raw_count,
        dedup_count=dedup_count,
        note="V1 Retrieval - raw OpenAlex results"
    )


    append_total_log(
        log_path=log_path,
        raw_count=raw_count,
        dedup_count=dedup_count
    )


    print(
        f"Saved: {log_path}"
    )



    print()

    print("#" * 70)
    print("# COMPLETED")
    print("#" * 70)


    print(
        "Database       : OpenAlex"
    )


    print(
        f"Query ID       : {QUERY_ID}"
    )


    if MAX_RECORDS is None:

        print(
            "Retrieval mode : ALL RESULTS"
        )

    else:

        print(
            f"Retrieval mode : MAX {MAX_RECORDS}"
        )


    print(
        f"Raw records    : {raw_count}"
    )


    print(
        f"After dedup    : {dedup_count}"
    )


    print(
        f"CSV            : {csv_path}"
    )


    print(
        f"Search log     : {log_path}"
    )


    print("#" * 70)


# 8. PROGRAM ENTRY POINT

if __name__ == "__main__":

    run_openalex_pipeline()
