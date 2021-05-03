from Charter import Charter
from elements.label import Label
from elements.line import Line
from point import Point
from tv_variables import Extend, Xloc, Color

myCharter = Charter("chartex2", 1000*60*60*24)
myLabel = Label(Point(1619168400000, 2000), "LINE IS HERE", xloc=Xloc.BAR_TIME, color=Color.MAROON, id="label1")
myLine = Line(Point(1619168400000, 2000), Point(1619268400000, 2500), extend=Extend.BOTH, color=Color.LIME)
myCharter.add_elements(myLabel, myLine)
myCharter.output_pinescript()