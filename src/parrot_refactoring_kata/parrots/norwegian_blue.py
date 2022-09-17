from parrot_refactoring_kata.parrot import Parrot


class NorwegianBlueParrot(Parrot):
    def speed(self) -> float:
        if self._nailed:
            return 0
        return self._compute_base_speed_for_voltage(self._voltage)
