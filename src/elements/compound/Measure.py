from elements.Element import Element
from PricePoint import PricePoint
from tv_variables import Color
from elements.Label import Label
from elements.Fill import Fill


class Measure(Element):
    def __init__(self, p1: PricePoint, p2: PricePoint) -> None:

        super().__init__(id)
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
