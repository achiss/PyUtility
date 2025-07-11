from uuid import uuid4
from uuid import UUID
from typing import TypeVar, Type

T: type = TypeVar('T', bound=Type[Exception])


def generate_uuid4(utility_exception: T) -> UUID:
    from PyUtility.src.processor_uid.script.exception_message import get_message, get_except_message

    try:
        return uuid4()

    except (OSError, TypeError) as e:
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
