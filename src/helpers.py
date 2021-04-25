def isNoneAny(*args) -> bool:
    "Returns True if any of the elements is None"
    for element in args:
        if element is None:
            return True
    return False

def roundTimestampToBar(timestamp: int, timeframe: int) -> int:
    return (timestamp//timeframe)*timeframe