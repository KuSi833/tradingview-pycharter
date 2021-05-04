from Charter import Charter
from elements.hline import Hline
from elements.label import Label
from elements.line import Line
from elements.fill import Fill
from point import Point
from tv_variables import Extend, LineStyle, Xloc, Color, HlineStyle

myCharter = Charter("chartex2", 1000 * 60 * 60 * 24)
myLabel = Label(Point(1619168400000, 2000), "placeholder",
                xloc=Xloc.BAR_TIME, color=Color.MAROON, id="label1")
hline1 = Hline(3500, color=Color.BLUE, linestyle=HlineStyle.DASHED, id="hline1")
hline2 = Hline(3000, color=Color.BLUE, linestyle=HlineStyle.DASHED, id="hline2")
fill = Fill(hline1=hline1, hline2=hline2, color=Color.BLUE, time_start=1618957756000, time_end=1619908156000)
myCharter.add_elements(myLabel, hline1, hline2, fill)
myCharter.output_pinescript()
