from Charter import Charter
from elements.hline import Hline
from elements.label import Label
from elements.line import Line
from point import Point
from tv_variables import Extend, LineStyle, Xloc, Color, HlineStyle

myCharter = Charter("chartex2", 1000 * 60 * 60 * 24)
myLabel = Label(Point(1619168400000, 2000), "LINE IS HERE",
                xloc=Xloc.BAR_TIME, color=Color.MAROON, id="label1")
# myLine = Line(Point(1619168400000, 2000), Point(1619268400000, 2500),
#               extend=Extend.BOTH, color=Color.LIME)
hline = Hline(3300, "bull go up", color=Color.GREEN, linestyle=HlineStyle.DASHED, id="hline1")
myCharter.add_elements(myLabel, hline)
myCharter.output_pinescript()
