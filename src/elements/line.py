from elements.Element import Element
from PricePoint import PricePoint
from constants.tv_constants import Color, Xloc, Extend, LineStyle
from helpers.formatting import parameter_formatting


class Line(Element):
    def __init__(self, p1: PricePoint, p2: PricePoint,
                 xloc: Xloc = Xloc.BAR_TIME,
                 extend: Extend = None,
                 color: Color = None,
                 style: LineStyle = None,
                 width: int = None,
                 id: str = None
                 ) -> None:

        super().__init__(id)
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
            f"x1={self.p1.timestamp}, y1={self.p1.price}, "
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
