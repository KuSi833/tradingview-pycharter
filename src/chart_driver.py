from Charter import Charter
from elements.Hline import Hline
from elements.Label import Label
from elements.Line import Line
from elements.Fill import Fill
from PricePoint import PricePoint
from elements.Plot import Plot
from elements.compound.Square import Square
from elements.compound.Measure import Measure
from tv_variables import Extend, LineStyle, Xloc, Color, HlineStyle

myCharter = Charter("chartex2", 1000 * 60 * 60 * 24)

myLabel = Label(PricePoint(1619168400000, 2000))
myMeasure = Measure(PricePoint(timestamp=1618957756000, price=4000),
                 PricePoint(timestamp=1619908156000, price=3000))

myCharter.add_elements(myLabel, myMeasure)
myCharter.output_pinescript()
