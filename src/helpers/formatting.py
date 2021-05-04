from enum import Enum
from typing import Union


def parameter_formatting(parameter: Union[bool, int, str, Enum], ps_parameter_name: str) -> str:
    "Given the paremeter and pinescript variable name, returns pinescript string"
    if parameter is None:  # None formatting
        return ""
    elif isinstance(parameter, bool):  # Boolean formatting
        return f", {ps_parameter_name} = {str(parameter).lower()}"
    elif isinstance(parameter, str):  # String formatting
        return f", {ps_parameter_name} = \"{parameter}\""
    elif isinstance(parameter, int):  # Integer formatting
        return f", {ps_parameter_name} = {parameter}"
    elif isinstance(parameter, Enum):  # Enum formatting
        return f", {ps_parameter_name} = {parameter.value}"
