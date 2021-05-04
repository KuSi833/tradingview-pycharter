from elements.Element import Element
from PricePoint import PricePoint
from elements.Line import Line
from constants.tv_constants import Color, LabelStyle, LineStyle
from elements.compound.Square import Square
from elements.Label import Label
from helpers.formatting import timestamp_to_string


class Measure(Element):
    def __init__(self, p1: PricePoint, p2: PricePoint) -> None:
        self.p1 = p1
        self.p2 = p2

        # Customisation
        # Colors
        profitcolor = Color.GREEN
        losscolor = Color.RED
        textcolor = Color.WHITE

        # Offset
        label_offset = 30

        # Testing for Measure Color
        if (p2.price >= p1.price):  # Profit
            self.color = profitcolor
            self.style = LabelStyle.LABEL_DOWN
            self.label_price = self.p2.price + label_offset
        else:  # Loss (never gonna happen)
            self.color = losscolor
            self.style = LabelStyle.LABEL_UP
            self.label_price = self.p2.price - label_offset

        # Label Text
        absolute_change = self.p2.price - self.p1.price
        if (p2.price >= p1.price):  # Profit
            percentage_change = f"{round(100 * (absolute_change / p1.price), 2)}%"
        else:  # Loss
            percentage_change = f"{round(100 * (absolute_change / p1.price), 2)}%"
        time = timestamp_to_string(self.p2.timestamp - self.p1.timestamp)
        self.label_text = (
            f"{round(absolute_change, 2)} ({percentage_change})\\n\\n"
            f"{time}"
        )

        # Base Element Scaffolding
        # Square
        self.square = Square(p1=p1, p2=p2, color=self.color, transp=80)

        # Lines
        self.midpoint_timestamp = (self.p1.timestamp + self.p2.timestamp) // 2
        self.midpoint_price = (self.p1.price + self.p2.price) // 2
        self.arrow_down = Line(PricePoint(timestamp=self.midpoint_timestamp, price=self.p1.price),
                               PricePoint(timestamp=self.midpoint_timestamp, price=self.p2.price),
                               color=self.color, style=LineStyle.ARROW_RIGHT)
        self.arrow_right = Line(PricePoint(timestamp=self.p1.timestamp, price=self.midpoint_price),
                                PricePoint(timestamp=self.p2.timestamp, price=self.midpoint_price),
                                color=self.color, style=LineStyle.ARROW_RIGHT)

        # Label
        self.label = Label(PricePoint(timestamp=self.midpoint_timestamp, price=self.label_price),
                           color=self.color, textcolor=textcolor, text=self.label_text, style=self.style)

    def to_pinescript(self):
        self.pine_instructions = ""

        self.pine_instructions += self.square.to_pinescript() + "\n"  # Square
        self.pine_instructions += self.arrow_down.to_pinescript() + "\n"  # Arrow Down
        self.pine_instructions += self.arrow_right.to_pinescript() + "\n"  # Arrow Right
        self.pine_instructions += self.label.to_pinescript() + "\n"  # Label

        return self.pine_instructions
