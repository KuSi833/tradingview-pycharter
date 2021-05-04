from elements.Element import Element
from tv_variables import Color, Xloc, Extend, LineStyle
from elements.Hline import Hline
from helpers.formatting import parameter_formatting


class Fill(Element):
    def __init__(self, hline1: Hline, hline2: Hline,
                 color: Color = Color.BLUE,
                 transp: int = None,
                 title: str = None,
                 editable: bool = None,
                 fillgaps: bool = None,
                 time_start: int = None,
                 time_end: int = None,
                 ) -> None:
        "Fills area between 2 horizontal lines, from time_start till time_end"

        self.hline1 = hline1
        self.hline2 = hline2
        self.color = color
        self.transp = transp
        self.title = title
        self.editable = editable
        self.fillgaps = fillgaps
        self.time_start = time_start
        self.time_end = time_end

    def time_interval_formatter(self) -> str:
        "Constructs pinescript for timerange filtering"
        if (self.time_start is None and self.time_end is None):
            return self.color.value
        elif (self.time_end is None):
            return f", color = time > {self.time_start} ? {self.color.value} : na"
        elif (self.time_start is None):
            return f", color = time < {self.time_start} ? {self.color.value} : na"
        else:
            return f", color = time > {self.time_start} ? (time < {self.time_end} ? {self.color.value} : na) : na"

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Required parameters
        self.pine_instruction += f"fill(hline1={self.hline1.id}, hline2={self.hline2.id}"

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
        self.pine_instruction += self.time_interval_formatter()

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction
