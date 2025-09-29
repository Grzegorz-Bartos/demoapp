from dataclasses import dataclass
from datetime import date
from typing import Optional

WEIGHTS = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


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

    if 1 <= mm <= 12:
        century = 1900
    elif 21 <= mm <= 32:
        century = 2000
        mm -= 20
    elif 81 <= mm <= 92:
        century = 1800
        mm -= 80
    elif 41 <= mm <= 52:
        century = 2100
        mm -= 40
    elif 61 <= mm <= 72:
        century = 2200
        mm -= 60
    else:
        return None

    year = century + yy
    try:
        return date(year, mm, dd)
    except ValueError:
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
