# from elements.Element import Element
# from PricePoint import PricePoint
# from tv_variables import Color
# from elements.Fill import Fill
# from elements.Label import Label
# from elements.Plot import Plot


# class Measure(Element):
#     def __init__(self, p1: PricePoint, p2: PricePoint) -> None:

#         super().__init__(id)
#         self.p1 = p1
#         self.p2 = p2

#         # Constants (can be modified)
#         self.profit_color: Color = Color.GREEN
#         self.loss_color: Color = Color.RED

#         # Testing for Measure Color
#         if (p2.price >= p1.price):  # Profit
#             self.color = self.profit_color
#         else:
#             self.color = self.loss_color

#         # Base Element Scaffolding

#         # Hlines
#         self.hline1 = Plot(self.p1.price, color=Color.NA)
#         self.hline2 = Plot(self.p2.price, color=Color.NA)

#         # Background coloring
#         self.fill = Fill(hl)
