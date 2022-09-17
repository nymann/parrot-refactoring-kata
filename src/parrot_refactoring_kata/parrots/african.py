from parrot_refactoring_kata.parrot import Parrot


class AfricanParrot(Parrot):
    def speed(self) -> float:
        return max(
            0,
            self._base_speed() - self._load_factor() * self._number_of_coconuts,
        )

    def _load_factor(self) -> float:
        return 9.0  # noqa: WPS432 magic-number
