import re
from exceptions import InvalidAttributeException, InvalidNameException
from tv_variables import colors, label_variables, line_variables, xlocs, hline_variables, tv_boolean

def validate_name(name: str) -> None:
    regex = "^[a-zA-Z_][a-zA-Z0-9_]*$"
    pattern = re.compile(regex)
    result = pattern.search(name)
    if result is None:
        raise InvalidNameException(f"Invalid name: {name}, should be of form: {regex}")

def validate_color(color: str) -> None:
    if color not in colors:
        regex = "^#[a-zA-Z0-9]{6}$"
        pattern = re.compile(regex)
        result = pattern.search(color)
        if result is None:
            raise InvalidNameException(f"Invalid color: {color}")

def validate_tv_bool(variable: str) -> None:
    if variable not in tv_boolean:
        raise InvalidAttributeException("Invalid form of boolean for tradingview")

def validate_xloc(xloc: str) -> None:
    if xloc not in xlocs:
        raise InvalidNameException(f"Invalid xloc: {xloc}")

# Label validation
def validate_yloc(yloc: str) -> None:
    if yloc not in label_variables["yloc"]:
        raise InvalidNameException(f"Invalid yloc: {yloc}")

def validate_label_style(label_style: str) -> None:
    if label_style not in label_variables["styles"]:
        raise InvalidNameException(f"Invalid label style: {label_style}")

def validate_size(size: str) -> None:
    if size not in label_variables["size"]:
        raise InvalidNameException(f"Invalid size: {size}")

def validate_textalign(textalign: str) -> None:
    if textalign not in label_variables["textalign"]:
        raise InvalidNameException(f"Invalid textalign: {textalign}")

# Line validation
def validate_line_style(line_style: str) -> None:
    if line_style not in line_variables["styles"]:
        raise InvalidNameException(f"Invalid line style: {line_style}")

def validate_extend(extend: str) -> None:
    if extend not in line_variables["extend"]:
        raise InvalidNameException(f"Invalid extend: {extend}")

# Hline validation
def validate_hline_style(hline_style: str) -> None:
    if hline_style not in hline_variables["styles"]:
        raise InvalidNameException(f"Invalid hline style: {hline_style}")