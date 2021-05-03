from elements.element import Element
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
                 id: str = None
                 ) -> None:
        super().__init__(id)
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

    def to_pinescript(self):
        self.pine_instruction: str = ""

        #Make sure script runs only once
        self.pine_instruction += f"if barstate.islast\n    "

        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        self.pine_instruction += (
            f"label.new(x={self.p.x}, y={self.p.y}, "
            f"text='{self.text}', "
            f"xloc={self.xloc.value}, "
            f"yloc={self.yloc.value}, "
            f"color={self.color.value}, "
            f"style={self.style.value}, "
            f"textcolor={self.textcolor.value}, "
            f"size={self.size.value}, "
            f"textalign={self.textalign.value}, "
            f"tooltip='{self.tooltip}'"
            f")"
        )

        return self.pine_instruction
