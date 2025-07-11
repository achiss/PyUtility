from typing import Any, Tuple

from bcrypt import gensalt, hashpw

from PyUtility.src.processor_password.script.config import SALT_ITERATION, ENCODING


def password_check(password_string: Any, password_length: int) -> Tuple[bool, str]:
    if password_length < 8:
        return False, f'incorrect password length {password_length}, should be greater 7 chars.'

    if not isinstance(password_string, str):
        return False, f'invalid "password" data type - expected string, got {type(password_string).__name__}.'

    password_string = password_string.strip()
    if len(password_string) == 0:
        return False, f'incorrect parameter "password_string", cannot be empty or whitespace.'

    return True, password_string


def password_conversion(password_string: str, encoding_type: str = ENCODING) -> Tuple[bool, bytes | str]:
    try:
        return True, password_string.encode(encoding=encoding_type)

    except UnicodeEncodeError:
        return False, 'encoding error'

    except LookupError:
        return False, f'unknown encoding, got {encoding_type}.'

    except Exception as e:
        return False, f'unexpected password conversion error - {e}'


def salt_parameter_check(): pass


def generate_salt(iteration: int = SALT_ITERATION) -> bytes: return gensalt(rounds=iteration)


def hash_it(password_string: str) -> Tuple[bool, str | bytes]:
    password_length: int = len(password_string)
    flag, password_result = password_check(password_string, password_length)
    if not flag:
        return False, password_result

    salt: bytes = generate_salt()
