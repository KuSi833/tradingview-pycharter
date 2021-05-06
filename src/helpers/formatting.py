from enum import Enum
from typing import Union

from constants.constants import Timeframe

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


def snap_to_timeframe(timestamp: int, timeframe: Union[Timeframe, int]) -> int:
    if (isinstance(timeframe, Timeframe) and (timestamp is not None)):
        return (timestamp // timeframe.value) * timeframe.value
    elif timestamp is not None:
        return (timestamp // timeframe) * timeframe


def timestamp_to_string(timestamp: int) -> str:
    days = timestamp // Timeframe.D1.value
    timestamp -= days * Timeframe.D1.value
    hours = timestamp // Timeframe.H1.value
    timestamp -= hours * Timeframe.H1.value
    minutes = timestamp // Timeframe.M1.value

    returnstring = ""
    if days > 0:
        returnstring += f"{days}d "
    if hours > 0:
        returnstring += f"{hours}h "
    if minutes > 0:
        returnstring += f"{minutes}m "

    return returnstring

def time_interval_formatter(time_start: int, time_end : int, color : str, add_comma: bool = True) -> str:
    returnstring = ""
    if add_comma:
        returnstring += ", "
    if (time_start is None and time_end is None):
            returnstring += f"color = {color}"
    elif (time_end is None):
            returnstring += f"color = time > {time_start} ? {color} : na"
    elif (time_start is None):
            returnstring += f"color = time <= {time_end} ? {color} : na"
    else:
            returnstring += f"color = time > {time_start} ? (time <= {time_end} ? {color} : na) : na"
    return returnstring