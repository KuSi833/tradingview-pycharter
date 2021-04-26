from Charter import Charter
from label import Label
from point import Point
from tv_variables import Color, Xloc

myCharter = Charter("chartex2", 1000*60*60)
myLabel = Label(Point(2000, 1619168400000), "test text", xloc=Xloc.BAR_TIME, color=Color.MAROON, initiate=True, id="label1")

print(myLabel)