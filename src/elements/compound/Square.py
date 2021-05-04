from elements.Element import Element
from PricePoint import PricePoint
from tv_variables import Color
from elements.Fill import Fill
from elements.Plot import Plot


class Square(Element):
    def __init__(self, p1: PricePoint, p2: PricePoint,
                 color: Color = None,
                 transp: int = None,
                 editable: bool = None,
                 id: str = None
                 ) -> None:

        super().__init__(id)
        self.p1 = p1
        self.p2 = p2
        self.color = color
        self.transp = transp
        self.editable = editable

        # Base Element Scaffolding

        # Hlines
        self.hline1 = Plot(self.p1.price, color=Color.NA, id="e1")  # Needs to be uniquely randomly generated
        self.hline2 = Plot(self.p2.price, color=Color.NA, id="e2")

        # Fill
        self.fill = Fill(e1=self.hline1, e2=self.hline2, color=self.color,
                         transp=self.transp, editable=self.editable,
                         time_start=self.p1.timestamp, time_end=self.p2.timestamp)

    def to_pinescript(self):
        self.pine_instructions = ""

        self.pine_instructions += self.hline1.to_pinescript() + "\n"
        self.pine_instructions += self.hline2.to_pinescript() + "\n"
        self.pine_instructions += self.fill.to_pinescript() + "\n"

        return self.pine_instructions
