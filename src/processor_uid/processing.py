from typing import overload
from typing import TypeVar, Type
from uuid import UUID

from PyUtility.src.processor_uid.script.generate_uuid4 import generate_uuid4
from PyUtility.src.processor_uid.script.generate_uuid5 import generate_uuid5

T: type = TypeVar('T', bound=Type[Exception])


@overload
def generate(utility_exception: T, as_string: bool = False) -> UUID | str: ...


@overload
def generate(domain: UUID, *name_parts: str | bytes, utility_exception: T, as_string: bool = False) -> UUID | str: ...


def generate(domain: UUID = None, *name_parts: str | bytes, utility_exception: T, as_string: bool = False) -> UUID | str:
    """"""

    try:
        if not domain:
            uid: UUID = generate_uuid4(utility_exception)

        else:
            uid: UUID = generate_uuid5(utility_exception, domain, *name_parts)

        if as_string:
            uid: str = str(uid)

        return uid

    except Exception as e:
        raise utility_exception(str(e)) from e


if __name__ == '__main__':
    id_1 = generate(utility_exception=Exception, as_string=True)
    print(id_1)
    print(type(id_1).__name__)

    id_result_1 = generate(id_1, '31', utility_exception=Exception)
    print(id_result_1)
    print(type(id_result_1).__name__)

    id_result_2 = generate(id_1, utility_exception=Exception, as_string=True)
    print(id_result_2)
    print(type(id_result_2).__name__)
