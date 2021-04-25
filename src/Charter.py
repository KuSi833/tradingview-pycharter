import input_validation
from exceptions import InvalidAttributeException, InvalidNameException
from helpers import isNoneAny


class Charter():
    def __init__(self, chart_name: str) -> None:
        self.set_chart_name(chart_name)
        self.instructions = []
        self.instructions.append(f"//@version=4")
        self.instructions.append(f"study('{chart_name}', overlay=true)")

    def set_chart_name(self, chart_name: str) -> None:
        input_validation.validate_chart_name(chart_name)
        self.chart_name = chart_name

    def draw_label(self, x: int, y: int,
                   text: str = "",
                   xloc: str = "bar_time",
                   y_pos: str = "price",
                   color: str = "color.blue",
                   style: str = "label.style_label_down",
                   textcolor: str = "color.black",
                   size: str = "normal",
                   textalign: str = "align_center",
                   tooltip: str = ""
                   ) -> None:
        """
            Draws label on Chart

            Args:
                x:  int
                    - index of bar        if xloc == "bar_index"
                    - UNIX timestamp      if xloc == "bar_time"
                y:  int
                    - price - ignored when y_pos is specified
                xloc: {"bar_index", "bar_time"}, optional, default="bar_time"
                    - if xloc == "bar_index" then x expects bar index
                    - if xloc == "bar_time"  then x expects UNIX timestamp
                y_pos: {"abovebar", "belowbar", "price"}, optional, defualt="price"
                    - position of label (up is above candle, down is below candle)

            Returns:
                None

            Raises:
                InvalidAttributeException: Invalid attribute name is given
        """
        # Value Validation
        input_validation.validate_color(color)
        input_validation.validate_color(textcolor)
        input_validation.validate_label_style(style)
        
        # PineScript Assembly
        label_instruction = []

        if xloc == "bar_time":
            label_instruction.append(f"if time == {x}")

        label_instruction.append(
            f"    "
            f"label.new({x}, {y}, "
            f"text='{text}', "
            f"xloc=xloc.{xloc}, "
            f"yloc=yloc.{y_pos}, "
            f"color={color}, "
            f"style={style}, "
            f"textcolor={textcolor}, "
            f"size=size.{size}, "
            f"textalign=text.{textalign}, "
            f"tooltip='{tooltip}'"
            f")"
        )
        self.instructions.extend(label_instruction)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int,
                  xloc: str = "bar_time",
                  extend: str = "none",
                  color: str = "blue",
                  style: str = "style_solid",
                  width: str = "1"
                  ) -> None:

        # Value Validation
        if isNoneAny(x1, y1, x2, y2):
            raise InvalidAttributeException(
                "All points need to be given")

        input_validation.validate_xloc(xloc)
        input_validation.validate_extend(extend)
        input_validation.validate_color(color)
        input_validation.validate_line_style(style)

        # PineScript Assembly
        line_instruction = []

        if xloc == "bar_time":
            if extend == "right":
                line_instruction.append(f"if time == {x1}")
            elif extend == "left":
                line_instruction.append(f"if time == {x2}")

        line_instruction.append(
            f"    " # Required distance for PineScript tab
            f"line.new(x1={x1}, y1={y1}, x2={x2}, y2={y2}, "
            f"xloc=xloc.{xloc}, extend=extend.{extend}, color=color.{color}, style=line.{style}, width={width})"
        )

        self.instructions.extend(line_instruction)

    def write_instructions(self):
        with open("instruction.pine", "w") as file:
            for instruction in self.instructions:
                file.write(instruction + "\n")
