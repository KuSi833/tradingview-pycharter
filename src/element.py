from input_validation import validate_name

class Element():
    def __init__(self, initiate: bool = False, id: str = None) -> None:
        "Base class of all elements on chart"
        self.initiate = initiate
        if self.initiate:
            if id is None:
                raise AttributeError("Id is required when initiate=True")
            self.set_id(id)

    def set_id(self, id):
        validate_name(id)
        self.id = id
