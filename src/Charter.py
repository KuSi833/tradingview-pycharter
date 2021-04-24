from input_validation import validate_chart_name
from exceptions import InvalidNameException

class Charter():
    def __init__(self, chart_name) -> None:
        self.set_chart_name(chart_name)
        self.instructions = [f'study["{chart_name}"]']

    def set_chart_name(self, chart_name):
        validate_chart_name(chart_name)
        self.chart_name = chart_name


