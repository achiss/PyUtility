from uuid import uuid5
from uuid import UUID
from typing import TypeVar, Tuple

from .config import UUID_REGEX

T: type = TypeVar('T')


def check_domain(domain: UUID | str) -> Tuple[bool, bool | str]:
    if isinstance(domain, UUID):
        return True, True

    elif isinstance(domain, str):
        return (True, False) if bool(UUID_REGEX.match(domain)) else (False, f'')

    return False, f''


def convert_domain(domain: str) -> UUID: return UUID(domain)


def check_name_part(*name_part: str | bytes) -> Tuple[bool, bool | str]:
    if len(name_part) < 1:
        return False, ''


def convert_name_part(*name_part: str | bytes) -> bytes:
    pass


def generate_uuid5() -> UUID:
    try:
        pass

    except Exception as e:
        pass
