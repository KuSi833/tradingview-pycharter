from elements.Element import Element
from tv_variables import Color, Xloc, Extend, LineStyle
from elements.Hline import Hline
from elements.Plot import Plot
from helpers.formatting import parameter_formatting
from typing import Union, Optional


class Fill(Element):
    def __init__(self, e1: Union[Plot, Hline], e2: Union[Plot, Hline],
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

        self.e1 = e1
        self.e2 = e2
        self.color = color
        self.transp = transp
        self.title = title
        self.editable = editable
        self.fillgaps = fillgaps
        self.show_last = showlast
        self.time_start = time_start
        self.time_end = time_end

        self.check_if_elements_match()

    def check_if_elements_match(self) -> None:
        if (isinstance(self.e1, Plot) and not isinstance(self.e2, Plot)):
            raise TypeError("Both elements need to be of the same type")
        if (isinstance(self.e1, Hline) and not isinstance(self.e2, Hline)):
            raise TypeError("Both elements need to be of the same type")

    def time_interval_formatter(self) -> str:
        "Constructs pinescript for timerange filtering"
        assert(isinstance(self.color, Color))  # Makes MyPy happy (Doesn't understand the checking if not None)

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
            self.pine_instruction += self.time_interval_formatter()

        # Special parameter if elements are of type Plot
        self.pine_instruction += parameter_formatting(self.show_last, "show_last")

        # End of pine instruction
        self.pine_instruction += ")"

        return self.pine_instruction
