# Multi-Source Citation Snowballing Collector

Citation-graph collector for the SLR project.

ACM Digital Library remains the assigned primary database. ACM currently blocks automated collection with verification/403, so this tool does **not** bypass ACM access controls. Instead, it uses independent citation-graph APIs only as technical discovery backends:

- **OpenCitations Index V2**: backward references and forward citations.
- **OpenAlex**: backward references and forward citations.
- **Crossref REST**: backward references and DOI metadata.

The sources are merged and deduplicated within each seed/direction by DOI. The output is a candidate list only; it does not make screening decisions. The script also computes a second global DOI-level deduplication count for the candidate set.

## Setup

From the repository root:

```powershell
python -m pip install -r .\\tools\\acm-snowballing\\requirements.txt
```

Test one seed:

```powershell
python .\\tools\\acm-snowballing\\run.py --limit 1
```

Test a specific seed:

```powershell
python .\\tools\\acm-snowballing\\run.py --seed ACM-001
```

Run all 46 current V2-INCLUDE seeds:

```powershell
python .\\tools\\acm-snowballing\\run.py
```

Validate an existing `snowballing-candidates.csv` **without calling any citation APIs**:

```powershell
python .\\tools\\acm-snowballing\\run.py --validate-existing
```

## Output

Writes:

`Ngo Minh Tien/SLR/snowballing-candidates.csv`

Important fields include:

- `seed_record_id`
- `direction` (BACKWARD/FORWARD)
- `doi`
- `source` (OpenAlex/OpenCitations/Crossref, possibly combined)
- `already_in_primary_csv`
- `collection_status`

The tool does **not** modify V1/V2 decisions, `03_final_included.csv`, `search-log.md`, or `prisma-flow.md`.

The summary distinguishes these levels:

- `Collected citation rows after per-seed/direction DOI deduplication`: rows written to the candidate CSV.
- `Global unique candidates after DOI deduplication`: one row per discovered DOI across all seeds/directions.
- `Already matched to primary corpus`: global candidates whose DOI or normalized title is already present in the primary corpus.
- `New snowballing candidates requiring V1 screening`: global unique candidates not already in the primary corpus.

## Interpretation

ACM Digital Library is still the database used for the team's assigned primary search. OpenCitations, OpenAlex, and Crossref are only citation-discovery backends. Their results are not assumed to equal ACM's complete References/Cited By lists.

A candidate discovered here must still be:

1. deduplicated against the SLR records;
2. V1 screened;
3. V2 full-text screened when eligible;
4. added to `03_final_included.csv` only if it passes V2.

The script also reports collection issues when a source cannot resolve a seed DOI or returns no citation rows.

