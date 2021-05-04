from elements.Element import Element
from PricePoint import PricePoint
from constants.tv_constants import Color, Display, PlotStyle, Series, Xloc, Extend, LineStyle
from helpers.formatting import parameter_formatting
from typing import Union, Any


class Plot(Element):
    def __init__(self, series: Union[Series, int, Any],
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
        super().__init__(id)
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
        self.pine_instruction += parameter_formatting(self.series, "series", add_comma=False)

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
