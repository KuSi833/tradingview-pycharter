from elements.element import Element
from PricePoint import PricePoint
from tv_variables import Color, LabelStyle, Size, TextAlign, Xloc, Yloc
from helpers.formatting import parameter_formatting


class Label(Element):
    def __init__(self, p: PricePoint,
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
        super().__init__(id)
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

        # Required parameter
        self.pine_instruction += (
            f"label.new(x={self.p.timestamp}, y={self.p.price}"
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
