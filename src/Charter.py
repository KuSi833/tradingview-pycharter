from input_validation import validate_chart_name
from exceptions import InvalidAttributeException, InvalidNameException
from helpers import isNoneAny


class Charter():
    def __init__(self, chart_name: str) -> None:
        self.set_chart_name(chart_name)
        self.instructions = []
        self.instructions.append(f"//@version=4")
        self.instructions.append(f"study('{chart_name}', overlay=true)")

    def set_chart_name(self, chart_name: str) -> None:
        validate_chart_name(chart_name)
        self.chart_name = chart_name

    def draw_label(self, x: int, y: int,
                   text: str = "",
                   x_measure: str = "bar_time",
                   y_pos: str = "price",
                   colour: str = "blue",
                   style: str = "style_label_down",
                   textcolor: str = "black",
                   size: str = "normal",
                   textalign: str = "align_center",
                   tooltip: str = ""
                   ) -> None:
        """
            Draws label on Chart

            Args:
                x:  int
                    - index of bar        if x_measure == "bar_index"
                    - UNIX timestamp      if x_measure == "bar_time"
                y:  int
                    - price - ignored when y_pos is specified
                x_measure: {"bar_index", "bar_time"}, optional, default="bar_time"
                    - if x_measure == "bar_index" then x expects bar index
                    - if x_measure == "bar_time"  then x expects UNIX timestamp
                y_pos: {"abovebar", "belowbar", "price"}, optional, defualt="price"
                    - position of label (up is above candle, down is below candle)

            Returns:
                None

            Raises:
                InvalidAttributeException: Invalid attribute name is given
        """
        label_instruction = (
            f"label.new({x}, {y}, "
            f"text='{text}', "
            f"xloc=xloc.{x_measure}, "
            f"yloc=yloc.{y_pos}, "
            f"color=color.{colour}, "
            f"style=label.{style}, "
            f"textcolor=color.{textcolor}, "
            f"size=size.{size}, "
            f"textalign=text.{textalign}, "
            f"tooltip='{tooltip}'"
            f")"
        )
        self.instructions.append(label_instruction)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int,
                  x_measure: str = "bar_time",
                  extend: str = "none",
                  colour: str = "blue",
                  style: str = "style_solid",
                  width: str = "1"
                  ) -> None:

        if isNoneAny(x1, y1, x2, y2):
            raise InvalidAttributeException(
                "All points need to be given")

        line_instruction = []
        
        if x_measure == "bar_time":
            if extend == "right":
                line_instruction.append(f"if time == {x1}")
            elif extend == "left":
                line_instruction.append(f"if time == {x2}")

        line_instruction.append(
            f"    " # Required distance for PineScript tab
            f"line.new(x1={x1}, y1={y1}, x2={x2}, y2={y2}, "
            f"xloc=xloc.{x_measure}, extend=extend.{extend}, color=color.{colour}, style=line.{style}, width={width})"
        )

        self.instructions.extend(line_instruction)

    def write_instructions(self):
        with open("instruction.pine", "w") as file:
            for instruction in self.instructions:
                file.write(instruction + "\n")
