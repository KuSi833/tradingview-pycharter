from elements.Element import Element
from PricePoint import PricePoint
from tv_variables import Color
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

    def to_pinescript(self):
        self.pine_instructions = ""

        self.pine_instructions += self.square.to_pinescript() + "\n"

        return self.pine_instructions
