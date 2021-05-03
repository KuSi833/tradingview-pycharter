from elements.element import Element
from tv_variables import Color, Xloc, Extend, LineStyle
from typing import Union
from elements.hline import Hline


class Fill(Element):
    def __init__(self, e1: Hline, e2: Hline,
                 color: Color = Color.BLUE,
                 transp: int = Xloc.BAR_TIME,
                 extend: Extend = Extend.NONE,
                 style: LineStyle = LineStyle.SOLID,
                 width: int = 1,
                 id: str = None
                 ) -> None:

        super().__init__(id)
        self.e1 = e1
        self.e2 = e2
        self.xloc = xloc
        self.extend = extend
        self.color = color
        self.style = style
        self.width = width

    def to_pinescript(self):
        self.pine_instruction: str = ""

        # Make sure script runs only once
        self.pine_instruction += "if barstate.islast\n    "

        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        self.pine_instruction += (
            f"line.new(x1={self.p1.x}, y1={self.p1.y}, "
            f"x2={self.p2.x}, y2={self.p2.y}, "
            f"xloc={self.xloc.value}, "
            f"extend={self.extend.value}, "
            f"color={self.color.value}, "
            f"style={self.style.value}, "
            f"width={self.width}"
            f")"
        )

        return self.pine_instruction
