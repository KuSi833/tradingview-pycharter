from __future__ import annotations
from Charter import Charter
from PricePoint import PricePoint
from constants.constants import Timeframe
from elements.fundamental import Label
from elements.compound import Fill
from elements.fundamental import Hline
from elements.fundamental import Bgcolor
from elements.fundamental import Barcolor
from elements.compound import Measure
from constants.tv_constants import Color

timeframe: Timeframe = Timeframe.H1

myCharter = Charter("chartex2", timeframe)

#myLabel = Label(myCharter, PricePoint(1619168400000, 2000))
#measureProfit = Measure(p1=PricePoint(timestamp=1618999136000, price=2534.15),
#                        p2=PricePoint(timestamp=1618917756000, price=3020.52), charter=myCharter)
# measureLoss = Measure(myCharter, PricePoint(timestamp=1619117756000, price=3341.84),
#                       PricePoint(timestamp=1619899136000, price=2803.42))
hline1 = Hline(myCharter, price = 2500, id = "hline1" )
hline2 = Hline(myCharter, price = 2700, id = "hline2" )
Fill(myCharter, hline1, hline2, color = Color.BLUE, time_end= 1619624367000)
bgcol = Bgcolor(myCharter, Color.FUCHSIA, transp = 50,time_start=1619624367000, title = "Bg color")
barcol = Barcolor(myCharter, Color.MAROON, offset= 2)
myCharter.output_pinescript()
