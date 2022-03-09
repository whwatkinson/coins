from enum import Enum
from typing import Dict, Union


class CoinToBig(Exception):
    def __init__(self, coin_size: Union[float, int]):
        self.message = f"{coin_size} exceed the maximum coin holder"
        super().__init__(self.message)


class CoinHolder(Enum):

    A = "A - 39.5 +"
    B = "B - 39.5"
    C = "C - 37.5"
    D = "D - 35"
    E = "E - 32.5"
    F = "F - 30"
    G = "G - 27.5"
    H = "H - 25"
    I = "I - 22.5"
    J = "J - 20"


class Bounds:
    def __init__(
        self, holder_size: Union[float, int], lower_bound: float, upper_bound: float
    ):
        self.holder_size = holder_size
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __repr__(self) -> str:
        return f"{self.holder_size=}"


SIZE_MAP: Dict[CoinHolder, Bounds] = {
    CoinHolder.A: Bounds(39.5, 39.5, 50),
    CoinHolder.B: Bounds(39.5, 37.5, 39.4),
    CoinHolder.C: Bounds(37.5, 35, 37.4),
    CoinHolder.D: Bounds(35, 32.5, 34.9),
    CoinHolder.E: Bounds(32.5, 30, 32.4),
    CoinHolder.F: Bounds(30, 27.5, 29.9),
    CoinHolder.G: Bounds(27.5, 25, 27.4),
    CoinHolder.H: Bounds(25, 22.5, 24.9),
    CoinHolder.I: Bounds(22.5, 20, 22.4),
    CoinHolder.J: Bounds(20, 0.5, 19.9),
}


def assign_flip(coin_size: Union[float, int]) -> CoinHolder:

    for coin_holder, bounds in SIZE_MAP.items():

        if bounds.lower_bound <= coin_size <= bounds.upper_bound:
            return coin_holder

    else:
        raise CoinToBig(coin_size)
