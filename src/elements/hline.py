from elements.element import Element
from tv_variables import Color, HlineStyle, LineStyle


class Hline(Element):
    def __init__(self, price: int,
                 title: str = "",
                 color: Color = Color.BLUE,
                 linestyle: HlineStyle = HlineStyle.SOLID,
                 linewidth: int = 1,
                 editable: bool = True,
                 id: str = None
                 ) -> None:
        super().__init__(id)
        self.price = price
        self.title = title
        self.color = color
        self.linestyle = linestyle
        self.linewidth = linewidth
        self.editable = editable

    def to_pinescript(self):
        self.pine_instruction: str = ""

        if self.id is not None:
            self.pine_instruction += f"{self.id} = "

        self.pine_instruction += (
            f"hline(price={self.price}, "
            f"title='{self.title}', "
            f"color={self.color.value}, "
            f"linestyle={self.linestyle.value}, "
            f"linewidth={self.linewidth}, "
            f"editable={str(self.editable).lower()}"
            f")"
        )

        return self.pine_instruction
