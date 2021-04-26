from element import Element
from point import Point
from tv_variables import Color, LabelStyle, Size, TextAlign, Xloc, Yloc


class Label(Element):
    def __init__(self, p: Point,
                 text: str = "",
                 xloc: Xloc = Xloc.BAR_TIME,
                 yloc: Yloc = Yloc.PRICE,
                 color: Color = Color.BLUE,
                 style: LabelStyle = LabelStyle.LABEL_DOWN,
                 textcolor: Color = Color.BLACK,
                 size: Size = Size.NORMAL,
                 textalign: TextAlign = TextAlign.CENTER,
                 tooltip: str = "",
                 initiate: bool = False,
                 id: str = None
                 ) -> None:
        super().__init__(initiate, id)
        self.p = p
        self.text = text
        self.xloc = xloc
        self.yloc = yloc
        self.color = color
        self.style = style
        self.textcolor = textcolor
        self.size = size
        self.textalign = textalign
        self.tooltip = tooltip

        self.pineInstruction: str = ""

    def __str__(self):
        if self.xloc is Xloc.BAR_TIME:
            self.pineInstruction += f"if time == {self.p.x}\n    "

        if self.initiate:
            self.pineInstruction += f"{self.id} = "

        self.pineInstruction += (
            f"label.new(x={self.p.x}, y={self.p.y}, "
            f"text='{self.text}', "
            f"xloc={self.xloc}, "
            f"yloc={self.yloc}, "
            f"color={self.color}, "
            f"style={self.style}, "
            f"textcolor={self.textcolor}, "
            f"size={self.size}, "
            f"textalign={self.textalign}, "
            f"tooltip='{self.tooltip}'"
            f")"
        )

        return self.pineInstruction