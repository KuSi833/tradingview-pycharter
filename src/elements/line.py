from elements.element import Element
from point import Point
from tv_variables import Color, Xloc, Extend, LineStyle


class Line(Element):
    def __init__(self, p1: Point, p2: Point,
                 xloc: Xloc = Xloc.BAR_TIME,
                 extend: Extend = Extend.NONE,
                 color: Color = Color.BLUE,
                 style: LineStyle = LineStyle.SOLID,
                 width: int = 1,
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
