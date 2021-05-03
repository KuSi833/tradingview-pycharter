from input_validation import validate_name
from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, id: str = None) -> None:
        "Base class of all elements on chart"
        if id is None:
            self.id = None
        else:
            self.set_id(id)

    @abstractmethod
    def to_pinescript(self):
        pass

    def set_id(self, id):
        validate_name(id)
        self.id = id
