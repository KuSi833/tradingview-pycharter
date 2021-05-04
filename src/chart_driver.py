from Charter import Charter
from constants.constants import Timeframe
from elements.Hline import Hline
from elements.Label import Label
from elements.Line import Line
from elements.Fill import Fill
from PricePoint import PricePoint
from elements.Plot import Plot
from elements.compound.Square import Square
from elements.compound.Measure import Measure
from constants.tv_constants import Extend, LineStyle, Xloc, Color, HlineStyle
from helpers.formatting import snap_to_timeframe as snap

timeframe: Timeframe = Timeframe.H1

myCharter = Charter("chartex2", timeframe)

myLabel = Label(PricePoint(snap(1619168400000, timeframe), 2000))
measureProfit = Measure(PricePoint(timestamp=1618917756000, price=2534.15),
                        PricePoint(timestamp=1618999136000, price=3020.52))
myCharter.add_element(measureProfit)
# measureLoss = Measure(PricePoint(timestamp=1619117756000, price=3341.84),
#                       PricePoint(timestamp=1619899136000, price=2803.42))
# myCharter.add_element(measureLoss)

myCharter.add_elements(myLabel)
myCharter.output_pinescript()
