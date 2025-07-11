from typing import Any
from typing import overload


def convert(exception_object: Any) -> str: return str(exception_object)


@overload
def get_message(exception_object: Any) -> str: ...


@overload
def get_message(description: str, exception_object: Any) -> str: ...


def get_message(description: str = None, exception_object: Any = None) -> str:
    if not description:
        return f'Failed to generate UUID: {convert(exception_object)}.'

    else:
        description = description.strip()
        if len(description) == 0:
            return f'Failed to generate UUID: parameter "description" is specified incorrectly.'

        return f'Failed to generate UUID - {description}: {convert(exception_object)}.'


def get_except_message(exception_object: Any) -> str:
    """Message for """
    return f'Unexpected UUID generation message: {exception_object}.'
