from parrot_refactoring_kata.parrot import Parrot


class EuropeanParrot(Parrot):
    def speed(self) -> float:
        return self._base_speed()
