from re import compile
from re import Pattern


UUID_REGEX: Pattern = compile(
    r'^[a-fA-F0-9]{8}-'
    r'[a-fA-F0-9]{4}-'
    r'[1-5][a-fA-F0-9]{3}-'
    r'[89abAB][a-fA-F0-9]{3}-'
    r'[a-fA-F0-9]{12}$'
)


ENCODING: str = 'utf-8'
