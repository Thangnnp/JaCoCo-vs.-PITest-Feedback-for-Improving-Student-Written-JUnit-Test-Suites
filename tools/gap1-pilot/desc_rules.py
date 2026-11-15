"""Quy tắc đọc mô tả bài CodeNet: lấy Sample I/O và nhận diện bài không có đáp án duy nhất."""
import html, re

def extract_samples(page):
    """Cặp (Sample Input k, Sample Output k); AIZU dùng 'Output for the Sample Input k'."""
    def grab(head):
        found = {}
        for m in re.finditer(head + r"\s*(\d*)\s*</h\d>\s*(?:<[^>]+>\s*)*?<pre[^>]*>(.*?)</pre>",
                             page, flags=re.I | re.S):
            k = m.group(1) or "1"
            if k not in found:
                found[k] = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        return found
    ins = grab(r"(?<!for )(?<!for the )Sample Input")
    outs = grab(r"Sample Output")
    outs2 = grab(r"Output for (?:the )?Sample Input")
    for k, v in outs2.items():
        outs.setdefault(k, v)
    return [(ins[k], outs[k]) for k in sorted(ins, key=int) if k in outs]

# Bài có nhiều đáp án đúng, chấm số thực có sai số, hoặc tương tác: không so output trực tiếp được
SPECIAL_JUDGE = [
    r"absolute or relative error", r"relative or absolute error", r"absolute error", r"relative error",
    r"error (?:of|less than|not (?:greater|more) than|within)", r"10\s*\^?\s*\{?\s*-\s*\d",
    r"if there (?:are|is|exist) (?:multiple|several|more than one)", r"any of them", r"print any",
    r"may print any", r"output any", r"multiple (?:solutions|answers)", r"special judge", r"interactive",
    r"reactive", r"judge will", r"several (?:possible )?answers",
]
_SJ = re.compile("|".join(SPECIAL_JUDGE), re.I)

def english_text(page):
    m = re.search(r'<span class="lang-en">(.*?)</span>\s*$', page, re.S)
    t = m.group(1) if m else page
    return html.unescape(re.sub(r"<[^>]+>", " ", t))

def special_judge_reason(page):
    m = _SJ.search(english_text(page))
    return m.group(0) if m else ""
