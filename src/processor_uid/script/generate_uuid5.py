from uuid import uuid5
from uuid import UUID
from typing import TypeVar, Type, Tuple

from PyUtility.src.processor_uid.script.config import UUID_REGEX, ENCODING

T: type = TypeVar('T', bound=Type[Exception])


def domain_check(domain: UUID | str) -> Tuple[bool, bool | str]:
    if isinstance(domain, str):
        return (True, False) if bool(UUID_REGEX.match(domain)) else (False, 'invalid UUID string format')

    elif isinstance(domain, UUID):
        return True, True

    else:
        return False, f'invalid parameter "domain" data type - expected string or UUID, got {type(domain).__name__}'


def domain_normalization(domain: UUID | str) -> UUID:
    flag, result = domain_check(domain)
    if not flag:
        raise ValueError(result)

    return domain if result else UUID(domain)


def name_parts_check(*name_parts: str | bytes) -> Tuple[bool, str | None]:
    if len(name_parts) < 1:
        return False, 'invalid parameter "name_parts" - at least one part must be provided'

    for count, name in enumerate(name_parts, 1):
        if not isinstance(name, (str, bytes)):
            return False, f'invalid parameter "name_parts" data type - expected string or bytes, got {type(name).__name__}'

    return True, None


def name_parts_normalization(encoding_type: str, *name_parts: str | bytes) -> bytes:
    flag, result = name_parts_check(*name_parts)

    if not flag:
        raise ValueError(result)

    name_list = []
    for name in name_parts:
        if isinstance(name, str):
            name_list.append(name.encode(encoding=encoding_type))

        else:
            name_list.append(name)

    return b''.join(name_list)


def generate_uuid5(utility_exception: T,
                   domain: UUID | str = None,
                   *name_parts: str | bytes) -> UUID:
    from PyUtility.src.processor_uid.script.exception_message import get_message, get_except_message

    try:
        domain_result: UUID = domain_normalization(domain)
        name_result: bytes = name_parts_normalization(ENCODING, *name_parts)

        return uuid5(namespace=domain_result, name=name_result)

    except (OSError, TypeError, ValueError) as e:
        try:
            msg: str = get_message(exception_object=e)
            raise utility_exception(msg)

        except Exception as inner_e:
            raise utility_exception(get_except_message(exception_object=inner_e)) from inner_e

    except Exception as e:
        try:
            msg: str = get_message(description='unexpected error', exception_object=e)
            raise utility_exception(msg)

        except Exception as inner_e:
            raise utility_exception(get_except_message(exception_object=inner_e)) from inner_e
