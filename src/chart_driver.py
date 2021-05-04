from Charter import Charter
from elements.Hline import Hline
from elements.Label import Label
from elements.Line import Line
from elements.Fill import Fill
from PricePoint import PricePoint
from tv_variables import Extend, LineStyle, Xloc, Color, HlineStyle

myCharter = Charter("chartex2", 1000 * 60 * 60 * 24)
myLabel = Label(PricePoint(1619168400000, 2000))
hline1 = Hline(3500, color=Color.BLUE,
               linestyle=HlineStyle.DASHED, id="hline1")
hline2 = Hline(3000, color=Color.BLUE,
               linestyle=HlineStyle.DASHED, id="hline2")
fill = Fill(hline1=hline1, hline2=hline2, color=Color.BLUE,
            time_start=1618957756000, time_end=1619908156000)
line1 = Line(PricePoint(timestamp=1618957756000, price=3000),
             PricePoint(timestamp=1619908156000, price=3500))
myCharter.add_elements(myLabel, hline1, hline2, fill, line1)
myCharter.output_pinescript()
