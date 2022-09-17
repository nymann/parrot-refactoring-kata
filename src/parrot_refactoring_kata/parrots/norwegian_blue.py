from parrot_refactoring_kata.parrot import Parrot


class NorwegianBlueParrot(Parrot):
    def speed(self) -> float:
        if self._nailed:
            return 0
        return min([24.0, self._voltage * self._base_speed()])
