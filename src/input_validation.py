import re
from exceptions import InvalidNameException
from tv_variables import colors

def validate_chart_name(chart_name: str) -> None:
    regex = "^[a-zA-Z_][a-zA-Z0-9_]*$"
    pattern = re.compile(regex)
    result = pattern.search(chart_name)
    if result is None:
        raise InvalidNameException(f"Invalid chart name, should be of form: {regex}")

def validate_colour(color: str) -> None:
    if color not in colors:
        regex = "^#[a-zA-Z0-9]{6}$"
        pattern = re.compile(regex)
        result = pattern.search(color)
        if result is None:
            raise InvalidNameException("Invalid color")