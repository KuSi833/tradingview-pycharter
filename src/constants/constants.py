from enum import Enum


class Timeframe(Enum):  # in ms
    S15 = 15 * 1000
    M1 = 60 * 1000
    M5 = 5 * 60 * 1000
    M15 = 15 * 60 * 1000
    H1 = 60 * 60 * 1000
    H4 = 4 * 60 * 60 * 1000
    D1 = 24 * 60 * 60 * 1000
