from re import compile, template


UUID_REGEX: template = compile(
    r'^[a-fA-F0-9]{8}-'
    r'[a-fA-F0-9]{4}-'
    r'5[a-fA-F0-9]{3}-'
    r'[89abAB][a-fA-F0-9]{3}-'
    r'[a-fA-F0-9]{12}$'
)
