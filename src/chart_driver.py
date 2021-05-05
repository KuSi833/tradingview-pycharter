from __future__ import annotations
from Charter import Charter
from PricePoint import PricePoint
from constants.constants import Timeframe
from elements.fundamental import Label
from elements.compound import Measure
from helpers.formatting import snap_to_timeframe as snap

timeframe: Timeframe = Timeframe.H1

myCharter = Charter("chartex2", timeframe)

myLabel = Label(myCharter, PricePoint(snap(1619168400000, timeframe), 2000))
measureProfit = Measure(myCharter, PricePoint(timestamp=1618917756000, price=2534.15),
                        PricePoint(timestamp=1618999136000, price=3020.52))
# measureLoss = Measure(myCharter, PricePoint(timestamp=1619117756000, price=3341.84),
#                       PricePoint(timestamp=1619899136000, price=2803.42))

myCharter.output_pinescript()
