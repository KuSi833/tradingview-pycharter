from enum import Enum, unique


@unique
class Color(Enum):
    BLACK = "color.black"
    BLUE = "color.blue"
    FUCHSIA = "color.fuchsia"
    GRAY = "color.gray"
    GREEN = "color.green"
    LIME = "color.lime"
    MAROON = "color.maroon"
    NAVY = "color.navy"
    OLIVE = "color.olive"
    ORANGE = "color.orange"
    PURPLE = "color.purple"
    RED = "color.red"
    SILVER = "color.silver"
    TEAL = "color.teal"
    WHITE = "color.white"
    YELLOW = "color.yellow"


@unique
class LabelStyle(Enum):
    NONE = "label.style_none"
    XCROSS = "label.style_xcross"
    CROSS = "label.style_cross"
    TRIANGLE_UP = "label.style_triangleup"
    TRIANGLE_DOWN = "label.style_triangledown"
    FLAG = "label.style_flag"
    CIRCLE = "label.style_circle"
    ARROW_UP = "label.style_arrowup"
    ARROW_DOWN = "label.style_arrowdown",
    LABEL_UP = "label.style_label_up"
    LABEL_DOWN = "label.style_label_down"
    LABEL_LEFT = "label.style_label_left"
    LABEL_RIGHT = "label.style_label_right"
    LABEL_LOWER_LEFT = "label.style_label_lower_left"
    LABEL_LOWER_RIGHT = "label.style_label_lower_right"
    LABEL_UPPER_LEFT = "label.style_label_upper_left"
    LABEL_UPPER_RIGHT = "label.style_label_upper_right"
    LABEL_CENTER = "label.style_label_center",
    SQUARE = "label.style_square"
    DIAMONG = "label.style_diamond"


@unique
class Size(Enum):
    AUTO = "size.auto"
    TINY = "size.tiny"
    SMALL = "size.small"
    NORMAL = "size.normal"
    LARGE = "size.large"
    HUGE = "size.huge"


@unique
class TextAlign(Enum):
    LEFT = "text.align_left"
    CENTER = "text.align_center"
    RIGHT = "text.align_right"


@unique
class Xloc(Enum):
    BAR_INDEX = "xloc.bar_index"
    BAR_TIME = "xloc.bar_time"


@unique
class Yloc(Enum):
    PRICE = "yloc.price"
    ABOVEBAR = "yloc.abovebar"
    BELOWBAR = "yloc.belowbar"
