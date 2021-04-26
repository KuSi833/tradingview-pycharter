import input_validation
from element import Element
from typing import List

class Charter():
    def __init__(self, chart_name: str, timeframe: int) -> None:
        self.set_chart_name(chart_name)
        self.timeframe = timeframe

        # Initialising element field
        self.objects = List[Element]

        # self.instructions = []
        # self.instructions.append(f"//@version=4")
        # self.instructions.append(f"study('{chart_name}', overlay=true)")

    def set_chart_name(self, chart_name: str) -> None:
        input_validation.validate_name(chart_name)
        self.chart_name = chart_name

    def add_element(self, element: Element) -> None:
        self.objects.append("test")