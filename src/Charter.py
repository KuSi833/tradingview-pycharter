import input_validation
from exceptions import InvalidAttributeException, InvalidNameException
from helpers import isNoneAny, roundTimestampToBar


class Charter():
    def __init__(self, chart_name: str, timeframe: int) -> None:
        self.set_chart_name(chart_name)
        self.timeframe = timeframe
        self.instructions = []
        self.instructions.append(f"//@version=4")
        self.instructions.append(f"study('{chart_name}', overlay=true)")

    def set_chart_name(self, chart_name: str) -> None:
        input_validation.validate_chart_name(chart_name)
        self.chart_name = chart_name

    def write_instructions(self):
        with open("instruction.pine", "w") as file:
            for instruction in self.instructions:
                file.write(instruction + "\n")

    # Fundamental drawings
    def draw_label(self, x: int, y: int,
                   text: str = "",
                   xloc: str = "xloc.bar_time",
                   yloc: str = "yloc.price",
                   color: str = "color.blue",
                   style: str = "label.style_label_down",
                   textcolor: str = "color.black",
                   size: str = "size.normal",
                   textalign: str = "text.align_center",
                   tooltip: str = ""
                   ) -> None:
        """
            Draws label on Chart

            Args:
                x:  int
                    - index of bar        if xloc == "bar_index"
                    - UNIX timestamp      if xloc == "bar_time"
                y:  int
                    - price - ignored when yloc is specified
                xloc: {"bar_index", "bar_time"}, optional, default="bar_time"
                    - if xloc == "bar_index" then x expects bar index
                    - if xloc == "bar_time"  then x expects UNIX timestamp
                yloc: {"abovebar", "belowbar", "price"}, optional, defualt="price"
                    - position of label (up is above candle, down is below candle)

            Returns:
                None

            Raises:
                InvalidAttributeException: Invalid attribute name is given
        """
        # Value Validation
        input_validation.validate_xloc(xloc)
        input_validation.validate_yloc(yloc)
        input_validation.validate_color(color)
        input_validation.validate_label_style(style)
        input_validation.validate_color(textcolor)
        input_validation.validate_size(size)
        input_validation.validate_textalign(textalign)

        # PineScript Assembly
        label_instruction = []

        if xloc == "xloc.bar_time":
            label_instruction.append(f"if time == {x}")

        label_instruction.append(
            f"    "
            f"label.new(x={x}, y={y}, "
            f"text='{text}', "
            f"xloc={xloc}, "
            f"yloc={yloc}, "
            f"color={color}, "
            f"style={style}, "
            f"textcolor={textcolor}, "
            f"size={size}, "
            f"textalign={textalign}, "
            f"tooltip='{tooltip}'"
            f")"
        )
        self.instructions.extend(label_instruction)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int,
                  xloc: str = "xloc.bar_time",
                  extend: str = "extend.none",
                  color: str = "color.blue",
                  style: str = "line.style_solid",
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

        if xloc == "xloc.bar_time":  # Needs rounding otherwise if will never be satisfied
            if extend == "extend.left":
                line_instruction.append(
                    f"if time == {roundTimestampToBar(x2, self.timeframe)}")
            else:
                line_instruction.append(
                    f"if time == {roundTimestampToBar(x1, self.timeframe)}")

        line_instruction.append(
            f"    "  # Required distance for PineScript tab
            f"line.new(x1={x1}, y1={y1}, x2={x2}, y2={y2}, "
            f"xloc={xloc}, extend={extend}, color={color}, style={style}, width={width})"
        )

        self.instructions.extend(line_instruction)

    # Derivative drawings
    def draw_horizontal_ray(self, x: int, y: int,
                            direction: str,
                            xloc: str = "xloc.bar_time",
                            color: str = "color.blue",
                            style: str = "line.style_solid",
                            width: str = "1"
                            ) -> None:
        "Draws horizontal ray with options to extend it right or left"
        if (direction == "right"):
            self.draw_line(x1=x, y1=y, x2=x+1, y2=y, xloc=xloc,
                           extend="extend.right", color=color, style=style, width=width)
        elif (direction == "left"):
            self.draw_line(x1=x, y1=y, x2=x+1, y2=y, xloc=xloc,
                           extend="extend.left", color=color, style=style, width=width)

    def draw_horizontal_line(self, x: int, y: int,
                             xloc: str = "xloc.bar_time",
                             color: str = "color.blue",
                             style: str = "line.style_solid",
                             width: str = "1"
                             ) -> None:
        "Draws horizontal line"
        self.draw_line(x1=x, y1=y, x2=x+1, y2=y, xloc=xloc,
                       extend="extend.both", color=color, style=style, width=width)

    def draw_vertical_line(self, x: int, y: int,
                           xloc: str = "xloc.bar_time",
                           color: str = "color.blue",
                           style: str = "line.style_solid",
                           width: str = "1"
                           ) -> None:
        "Draws vertical line"
        self.draw_line(x1=x, y1=y, x2=x, y2=y + "+1", xloc=xloc,
                       extend="extend.both", color=color, style=style, width=width)
