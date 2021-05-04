from elements.element import Element
from tv_variables import Color, HlineStyle, LineStyle
from helpers.formatting import parameter_formatting


class Hline(Element):
    def __init__(self, price: int,
                 title: str = None,
                 color: Color = None,
                 linestyle: HlineStyle = None,
                 linewidth: int = None,
                 editable: bool = None,
                 id: str = None
                 ) -> None:
        super().__init__(id)
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

        # Required parameter
        self.pine_instruction += (
            f"hline(price={self.price}"
        )

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
