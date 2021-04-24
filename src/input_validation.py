import re
from exceptions import InvalidNameException

def validate_chart_name(chart_name: str) -> bool:
    regex = "^[a-zA-Z_][a-zA-Z0-9_]*$"
    pattern = re.compile(regex)
    result = pattern.search(chart_name)
    if result is None:
        raise InvalidNameException(f"Invalid chart name, should be of form: {regex}")