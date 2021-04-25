def isNoneAny(*args) -> bool:
    "Returns True if any of the elements is None"
    for element in args:
        if element is None:
            return True
    return False