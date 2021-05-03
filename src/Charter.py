import input_validation
from elements.element import Element
from typing import List
from elements.label import Label


class Charter():
    def __init__(self, chart_name: str, timeframe: int) -> None:
        self.set_chart_name(chart_name)
        self.timeframe = timeframe

        # Initialising element field
        self.elements: List[Element] = []

        self.pine_instruction = (
            f"//@version=4\n"
            f"study('{chart_name}', overlay=true)"
        )

    def set_chart_name(self, chart_name: str) -> None:
        input_validation.validate_name(chart_name)
        self.chart_name = chart_name

    def add_element(self, element: Element) -> None:
        self.elements.append(element)

    def add_elements(self, *elements: Element) -> None:
        self.elements.extend(elements)

    def to_pinescript(self) -> str:
        return self.pine_instruction

    def output_pinescript(self) -> None:
        with open("instruction.pine", "w") as file:
            file.write(self.to_pinescript() + "\n")
            for element in self.elements:
                file.write(element.to_pinescript() + "\n")
