from __future__ import annotations
from Charter import Charter
from abc import ABC, abstractmethod
from typing import Union, Any
from helpers.formatting import parameter_formatting, snap_to_timeframe, time_interval_formatter
from helpers.input_validation import validate_name
from PricePoint import PricePoint
from constants.tv_constants import Color, LabelStyle, Size, TextAlign, Xloc, Yloc
from constants.tv_constants import HlineStyle, LineStyle, Extend, PlotStyle, Series, Display
from helpers.formatting import time_interval_formatter


class Element(ABC):
    def __init__(self, charter: Charter, id: str = None) -> None:
        "Base class of all elements on chart"
        self.charter = charter
        if id is None:
            self.id = None
        else:
            self.set_id(id)
        charter.add_element(self)

    @abstractmethod
    def to_pinescript(self):
        pass

    def set_id(self, id):
        validate_name(id)
        self.id = id


class Label(Element):
    def __init__(self, charter: Charter, p: PricePoint,
                 text: str = None,
                 xloc: Xloc = Xloc.BAR_TIME,
                 yloc: Yloc = None,
                 color: Color = None,
                 style: LabelStyle = None,
                 textcolor: Color = None,
                 size: Size = None,
                 textalign: TextAlign = None,
                 tooltip: str = None,
                 id: str = None
                 ) -> None:
        super().__init__(charter, id)
        self.p = p
        self.text = text
        self.xloc = xloc
        self.yloc = yloc
        self.color = color
        self.style = style
        self.textcolor = textcolor
        self.size = size
        self.textalign = textalign
        self.tooltip = tooltip

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Make sure script runs only once
        self.pine_instruction += "if barstate.islast\n    "

        # Initialisation
        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        # Pinescript function
        self.pine_instruction += "label.new("

        # Required parameter
        self.pine_instruction += (
            f"x={self.p.timestamp}, y={self.p.price}"
        )
        self.pine_instruction += parameter_formatting(self.xloc, "xloc")

        # Optional parameters
        parameters = [
            (self.text, "text"),
            (self.yloc, "yloc"),
            (self.color, "color"),
            (self.style, "style"),
            (self.textcolor, "textcolor"),
            (self.size, "size"),
            (self.textalign, "textalign"),
            (self.tooltip, "tooltip")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction


class Line(Element):
    def __init__(self, charter: Charter, p1: PricePoint, p2: PricePoint,
                 xloc: Xloc = Xloc.BAR_TIME,
                 extend: Extend = None,
                 color: Color = None,
                 style: LineStyle = None,
                 width: int = None,
                 id: str = None
                 ) -> None:

        super().__init__(charter, id)
        self.p1 = p1
        self.p2 = p2
        self.xloc = xloc
        self.extend = extend
        self.color = color
        self.style = style
        self.width = width

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Make sure script runs only once
        self.pine_instruction += "if barstate.islast\n    "

        # Initialisation
        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        # Pinescript function
        self.pine_instruction += "line.new("

        # Required parameters
        self.pine_instruction += (
            f"x1={snap_to_timeframe(self.p1.timestamp, self.charter.get_timeframe())}, y1={self.p1.price}, "
            f"x2={snap_to_timeframe(self.p2.timestamp, self.charter.get_timeframe())}, y2={self.p2.price}, "
            f"xloc={self.xloc.value}"
        )

        # Optional parameters
        parameters = [
            (self.extend, "extend"),
            (self.color, "color"),
            (self.style, "style"),
            (self.width, "width")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction


class Hline(Element):
    def __init__(self, charter: Charter, price: int,
                 title: str = None,
                 color: Color = None,
                 linestyle: HlineStyle = None,
                 linewidth: int = None,
                 editable: bool = None,
                 id: str = None
                 ) -> None:
        super().__init__(charter, id)
        self.price = price
        self.title = title
        self.color = color
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.editable = editable

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Initialisation
        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        # Pinescript function
        self.pine_instruction += "hline("

        # Required parameter
        self.pine_instruction += parameter_formatting(
            self.price, "price", add_comma=False)

        # Optional parameters
        parameters = [
            (self.title, "title"),
            (self.color, "color"),
            (self.linestyle, "linestyle"),
            (self.linewidth, "linewidth"),
            (self.editable, "editable")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction


class Plot(Element):
    def __init__(self, charter: Charter, series: Union[Series, int, Any],
                 title: str = None,
                 color: Color = None,
                 linewidth: int = None,
                 style: PlotStyle = None,
                 trackprice: bool = None,
                 histbase: float = None,
                 offset: int = None,
                 join: bool = None,
                 editable: bool = None,
                 show_last: int = None,
                 display: Display = None,
                 id: str = None
                 ) -> None:
        """
        Series can be any build in pinescript series, or a constant
        Any is also an otpion for more complex plotting, but no support for that is provided
        """
        super().__init__(charter, id)
        self.series = series
        self.title = title
        self.color = color
        self.linewidth = linewidth
        self.style = style
        self.trackprice = trackprice
        self.histbase = histbase
        self.offset = offset
        self.join = join
        self.editable = editable
        self.show_last = show_last
        self.display = display

    def to_pinescript(self):
        self.pine_instruction: str = ""
        # Initialisation
        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        # Pinescript function
        self.pine_instruction += "plot("

        # Required parameters
        self.pine_instruction += parameter_formatting(
            self.series, "series", add_comma=False)

        # Optional parameters
        parameters = [
            (self.title, "title"),
            (self.color, "color"),
            (self.linewidth, "linewidth"),
            (self.style, "style"),
            (self.trackprice, "trackprice"),
            (self.histbase, "histbase"),
            (self.offset, "offset"),
            (self.join, "join"),
            (self.editable, "editable"),
            (self.show_last, "show_last"),
            (self.display, "display")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction


class Fill(Element):
    def __init__(self, charter: Charter, e1: Union[Plot, Hline], e2: Union[Plot, Hline],
                 color: Color = None,
                 transp: int = None,
                 title: str = None,
                 editable: bool = None,
                 fillgaps: bool = None,
                 showlast: int = None,
                 time_start: int = None,
                 time_end: int = None
                 ) -> None:
        "Fills area between 2 horizontal lines, from time_start till time_end"
        super().__init__(charter)
        self.e1 = e1
        self.e2 = e2
        self.color = color
        self.transp = transp
        self.title = title
        self.editable = editable
        self.fillgaps = fillgaps
        self.show_last = showlast
        self.time_start = snap_to_timeframe(time_start, self.charter.timeframe)
        self.time_end = snap_to_timeframe(time_end, self.charter.timeframe)

        self.check_if_elements_match()

    def check_if_elements_match(self) -> None:
        if (isinstance(self.e1, Plot) and not isinstance(self.e2, Plot)):
            raise TypeError("Both elements need to be of the same type")
        if (isinstance(self.e1, Hline) and not isinstance(self.e2, Hline)):
            raise TypeError("Both elements need to be of the same type")

    def time_range_filtering(self) -> str:
        "Constructs pinescript for timerange filtering"
        # Makes MyPy happy (Doesn't understand the checking if not None)
        assert(isinstance(self.color, Color))
        return time_interval_formatter(self.time_start, self.time_end, self.color.value)

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Pinescript function
        self.pine_instruction += "fill("

        # Required parameters - element type dependent
        if isinstance(self.e1, Hline):
            self.pine_instruction += f"hline1={self.e1.id}, hline2={self.e2.id}"
        else:
            self.pine_instruction += f"plot1={self.e1.id}, plot2={self.e2.id}"

        # Optional parameters
        parameters = [
            (self.transp, "transp"),
            (self.title, "title"),
            (self.editable, "editable"),
            (self.fillgaps, "fillgaps")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # Custom Color formatting for fill
        if self.color is not None:
            self.pine_instruction += self.time_range_filtering()

        # Special parameter if elements are of type Plot
        self.pine_instruction += parameter_formatting(
            self.show_last, "show_last")

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction


class Bgcolor(Element):
    def __init__(self, charter: Charter,
                 color: Color = None,
                 transp: int = None,
                 offset: int = None,
                 time_start: int = None,
                 time_end: int = None,
                 show_last: int = None,
                 title: str = None,
                 editable: bool = None) -> None:

        super().__init__(charter)
        self.color = color
        self.transp = transp
        self.offset = offset
        self.time_start = snap_to_timeframe(time_start, self.charter.timeframe)
        self.time_end = snap_to_timeframe(time_end, self.charter.timeframe)
        self.show_last = show_last
        self.editable = editable
        self.title = title

    def time_range_filtering(self) -> str:
        "Constructs pinescript for timerange filtering"
        # Makes MyPy happy (Doesn't understand the checking if not None)
        assert(isinstance(self.color, Color))
        return time_interval_formatter(self.time_start, self.time_end, self.color.value)

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Pinescript function
        self.pine_instruction += "bgcolor("

        # Required parameters
        self.pine_instruction += f"color={self.color.value}"

        # Optional parameters
        parameters = [
            (self.transp, "transp"),
            (self.offset, "offset"),
            (self.editable, "editable"),
            (self.show_last, "show_last"),
            (self.title, "title")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # Custom Color formatting for fill
        if self.color is not None:
            self.pine_instruction += self.time_range_filtering()

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction


class Barcolor(Element):
    def __init__(self, charter: Charter,
                 color: Color = None,
                time_start: int = None,
                 time_end: int = None,
                 offset: int = None,
                 editable: bool = None,
                 show_last: int = None,
                 title: str = None) -> None:
        super().__init__(charter)
        self.color = color
        self.time_start = snap_to_timeframe(time_start, self.charter.timeframe)
        self.time_end = snap_to_timeframe(time_end, self.charter.timeframe)
        self.offset = offset
        self.editable = editable
        self.show_last = show_last
        self.title = title

    def time_range_filtering(self) -> str:
        "Constructs pinescript for timerange filtering"
        # Makes MyPy happy (Doesn't understand the checking if not None)
        assert(isinstance(self.color, Color))
        return time_interval_formatter(self.time_start, self.time_end, self.color.value)
        
    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Pinescript function
        self.pine_instruction += "barcolor("

        # Required parameters
        self.pine_instruction += f"color={self.color.value}"

        # Optional parameters
        parameters = [
            (self.offset, "offset"),
            (self.editable, "editable"),
            (self.show_last, "show_last"),
            (self.title, "title")
        ]
        for parameter, ps_parameter_name in parameters:
            self.pine_instruction += parameter_formatting(
                parameter, ps_parameter_name)

        # Custom Color formatting 
        if self.color is not None:
            self.pine_instruction += self.time_range_filtering()
        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction
