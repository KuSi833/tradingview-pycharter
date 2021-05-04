from elements.Element import Element
from PricePoint import PricePoint
from tv_variables import Color, PlotStyle, Series, Xloc, Extend, LineStyle
from helpers.formatting import parameter_formatting
from typing import Union


class Plot(Element):
    def __init__(self, series: Union[Series, int, any],
                 title: str = None,
                 color: Color = None,
                 linewidth: int = None,
                 style: PlotStyle = None,

                 id: str = None
                 ) -> None:
        """
        Series can be any build in pinescript series, or a constant
        Any is also an otpion for more complex plotting, but no support for that is provided
        """

        super().__init__(id)
        self.series = series
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

        # Required parameters
        self.pine_instruction += (
            f"line.new(x1={self.p1.timestamp}, y1={self.p1.price}, "
            f"x2={self.p2.timestamp}, y2={self.p2.price}, "
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
