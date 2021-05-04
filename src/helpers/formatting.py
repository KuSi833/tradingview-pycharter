from enum import Enum
from typing import Union


def parameter_formatting(parameter: Union[bool, int, str, Enum], ps_parameter_name: str, add_comma: bool = True) -> str:
    """
    Given the paremeter and pinescript variable name, returns pinescript string
    add_coma = False used when parameter is function
    """
    returnstring = ""
    if add_comma:
        returnstring += ", "
    returnstring += f"{ps_parameter_name} = "

    if parameter is None:  # None formatting
        return ""
    elif isinstance(parameter, bool):  # Boolean formatting
        returnstring += str(parameter).lower()
    elif isinstance(parameter, str):  # String formatting
        returnstring += f"\"{parameter}\""
    elif isinstance(parameter, int) or isinstance(parameter, float):  # Integer and Float formatting
        returnstring += str(parameter)
    elif isinstance(parameter, Enum):  # Enum formatting
        returnstring += parameter.value

    return returnstring
