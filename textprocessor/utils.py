import random
import re

LATIN = r"A-Za-zÀ-ÖØ-öø-ÿĄąĆćĘęŁłŃńÓóŚśŹźŻż"
WORD_RE = re.compile(rf"[{LATIN}]{{4,}}", re.UNICODE)


def _shuffle_middle(s: str) -> str:
    if len(s) < 4:
        return s
    first, middle, last = s[0], list(s[1:-1]), s[-1]
    random.shuffle(middle)
    return first + "".join(middle) + last


def scramble_text(text: str) -> str:
    return WORD_RE.sub(lambda m: _shuffle_middle(m.group(0)), text)
