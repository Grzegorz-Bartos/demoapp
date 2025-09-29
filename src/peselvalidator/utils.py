from dataclasses import dataclass
from datetime import date
from typing import Optional, Tuple

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

CENTURY_OFFSETS: dict[Tuple[int, int], Tuple[int, int]] = {
    (1, 12): (1900, 0),
    (21, 32): (2000, 20),
    (81, 92): (1800, 80),
    (41, 52): (2100, 40),
    (61, 72): (2200, 60),
}


@dataclass
class PeselInfo:
    valid: bool
    birth_date: Optional[date] = None
    gender: Optional[str] = None
    error: Optional[str] = None


def _decode_birth_date(pesel: str) -> Optional[date]:
    yy = int(pesel[0:2])
    mm = int(pesel[2:4])
    dd = int(pesel[4:6])

    for (lo, hi), (century, offset) in CENTURY_OFFSETS.items():
        if lo <= mm <= hi:
            year = century + yy
            month = mm - offset
            try:
                return date(year, month, dd)
            except ValueError:
                return None
    return None


def _checksum_ok(pesel: str) -> bool:
    s = sum(int(d) * w for d, w in zip(pesel[:10], WEIGHTS))
    control = (10 - (s % 10)) % 10
    return control == int(pesel[10])


def validate_pesel(pesel: str) -> PeselInfo:
    if len(pesel) != 11 or not pesel.isdigit():
        return PeselInfo(False, error="PESEL musi mieć 11 cyfr")

    birth = _decode_birth_date(pesel)
    if birth is None:
        return PeselInfo(False, error="Niepoprawna data urodzenia w PESEL")

    if not _checksum_ok(pesel):
        return PeselInfo(False, error="Niepoprawna cyfra kontrolna")

    gender = "M" if int(pesel[9]) % 2 == 1 else "K"
    return PeselInfo(True, birth, gender)
