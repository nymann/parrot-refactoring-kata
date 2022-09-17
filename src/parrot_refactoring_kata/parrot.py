from abc import ABC
from abc import abstractmethod


class Parrot(ABC):
    def __init__(
        self,
        number_of_coconuts: int,
        voltage: int | float,
        nailed: bool,
    ) -> None:
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    @abstractmethod
    def speed(self) -> float:
        raise NotImplementedError

    def _base_speed(self) -> float:
        return 12.0  # noqa: WPS432 magic-number
