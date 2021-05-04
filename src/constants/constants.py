from enum import Enum


class Timeframe(Enum):
    S15 = 15
    M1 = 60
    M5 = 300
    M15 = 900
    H1 = 3600
    H4 = 14400
    D1 = 86400
