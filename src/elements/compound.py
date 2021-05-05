from __future__ import annotations
from PricePoint import PricePoint
from helpers.formatting import timestamp_to_string, snap_to_timeframe
from constants.tv_constants import Color, Display, LabelStyle, LineStyle
from elements.fundamental import Element, Fill, Plot, Label, Line


class Square(Element):
    def __init__(self, charter: Charter, p1: PricePoint, p2: PricePoint,
                 color: Color = None,
                 transp: int = None,
                 ) -> None:
        super().__init__(charter)
        if (p1.timestamp < p2.timestamp):
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1
        self.color = color
        self.transp = transp

        # Base Element Scaffolding

        # Hlines  TODO: Needs to be uniquely randomly generated
        self.hline1 = Plot(charter, self.p1.price, color=Color.NA, id="e1", editable=False, display=Display.NONE)
        self.hline2 = Plot(charter, self.p2.price, color=Color.NA, id="e2", editable=False, display=Display.NONE)

        # Fill
        self.fill = Fill(charter, e1=self.hline1, e2=self.hline2, color=self.color, transp=self.transp,
                         time_start=self.p1.timestamp, time_end=self.p2.timestamp)

    def to_pinescript(self):
        self.pine_instructions = "// Square"
        return self.pine_instructions


class Measure(Element):
    def __init__(self, charter: Charter, p1: PricePoint, p2: PricePoint) -> None:
        super().__init__(charter)
        self.p1 = p1
        self.p2 = p2

        # Customisation
        # Colors
        profitcolor = Color.GREEN
        losscolor = Color.RED
        textcolor = Color.WHITE

        # Offset
        label_offset = 30

        # Aligning timestamps - used for Charting
        aligned_timestamp1 = snap_to_timeframe(timestamp=self.p1.timestamp, timeframe=charter.get_timeframe())
        aligned_timestamp2 = snap_to_timeframe(timestamp=self.p2.timestamp, timeframe=charter.get_timeframe())

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

        time = self.p2.timestamp - self.p1.timestamp
        bars = time // charter.get_timeframe()
        self.label_text = (
            f"{round(absolute_change, 2)} ({percentage_change})\\n\\n"
            f"{bars} bars, {timestamp_to_string(time)}"
        )

        # Base Element Scaffolding
        # Square
        self.square = Square(charter, p1=p1, p2=p2, color=self.color, transp=80)

        # Lines
        self.midpoint_timestamp = (aligned_timestamp1 + aligned_timestamp2) // 2
        self.midpoint_price = (self.p1.price + self.p2.price) // 2
        self.arrow_down = Line(charter,
                               PricePoint(timestamp=self.midpoint_timestamp, price=self.p1.price),
                               PricePoint(timestamp=self.midpoint_timestamp, price=self.p2.price),
                               color=self.color, style=LineStyle.ARROW_RIGHT)
        self.arrow_right = Line(charter,
                                PricePoint(timestamp=aligned_timestamp1, price=self.midpoint_price),
                                PricePoint(timestamp=aligned_timestamp2, price=self.midpoint_price),
                                color=self.color, style=LineStyle.ARROW_RIGHT)

        # Label
        self.label = Label(charter, PricePoint(timestamp=self.midpoint_timestamp, price=self.label_price),
                           color=self.color, textcolor=textcolor, text=self.label_text, style=self.style)

    def to_pinescript(self):
        self.pine_instructions = "// Measure"
        return self.pine_instructions


from Charter import Charter
