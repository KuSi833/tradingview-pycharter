import re
from exceptions import InvalidNameException


def validate_name(name: str) -> None:
    regex = "^[a-zA-Z_][a-zA-Z0-9_]*$"
    pattern = re.compile(regex)
    result = pattern.search(name)
    if result is None:
        raise InvalidNameException(
            f"Invalid name: {name}, should be of form: {regex}")
