from uuid import uuid4
from uuid import UUID
from typing import TypeVar

T: type = TypeVar('T')


def generate_uuid4(utility_exception: T) -> UUID:
    try:
        return uuid4()

    except (OSError, TypeError) as e:
        raise utility_exception(f'Failed to generate UUID: {e}.') from e

    except Exception as e:
        raise utility_exception(f'Failed to generate UUID - unexpected error: {e}.') from e
