from elements.Element import Element
from PricePoint import PricePoint
from elements.Line import Line
from tv_variables import Color, LineStyle
from elements.compound.Square import Square


class Measure(Element):
    def __init__(self, p1: PricePoint, p2: PricePoint) -> None:

        self.p1 = p1
        self.p2 = p2

        # Constants (can be modified)
        self.profit_color: Color = Color.GREEN
        self.loss_color: Color = Color.RED

        # Testing for Measure Color
        if (p2.price >= p1.price):  # Profit
            self.color = self.profit_color
        else:
            self.color = self.loss_color

        # Base Element Scaffolding

        # Square
        self.square = Square(p1=p1, p2=p2, color=self.color)

        # Lines
        self.midpoint_timestamp = (self.p1.timestamp + self.p2.timestamp) // 2
        self.midpoint_price = (self.p1.price + self.p2.price) // 2

        self.arrow_down = Line(PricePoint(timestamp=self.midpoint_timestamp, price=self.p1.price),
                               PricePoint(timestamp=self.midpoint_timestamp, price=self.p2.price),
                               color=self.color, style=LineStyle.ARROW_RIGHT)
        self.arrow_right = Line(PricePoint(timestamp=self.p1.timestamp, price=self.midpoint_price),
                                PricePoint(timestamp=self.p2.timestamp, price=self.midpoint_price),
                                color=self.color, style=LineStyle.ARROW_RIGHT)

    def to_pinescript(self):
        self.pine_instructions = ""

        self.pine_instructions += self.square.to_pinescript() + "\n"  # Square
        self.pine_instructions += self.arrow_down.to_pinescript() + "\n"  # Arrow Down
        self.pine_instructions += self.arrow_right.to_pinescript() + "\n"  # Arrow Right

        return self.pine_instructions
