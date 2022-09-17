import pytest

from parrot_refactoring_kata.parrot import Parrot
from parrot_refactoring_kata.parrot import ParrotType

test_cases = [
    (Parrot(type_of_parrot=ParrotType.EUROPEAN, number_of_coconuts=0, voltage=0, nailed=False), 12.0),
    (Parrot(type_of_parrot=ParrotType.AFRICAN, number_of_coconuts=1, voltage=0, nailed=False), 3.0),
    (Parrot(type_of_parrot=ParrotType.AFRICAN, number_of_coconuts=2, voltage=0, nailed=False), 0),
    (Parrot(type_of_parrot=ParrotType.AFRICAN, number_of_coconuts=0, voltage=0, nailed=False), 12.0),
    (Parrot(type_of_parrot=ParrotType.NORWEGIAN_BLUE, number_of_coconuts=0, voltage=1.5, nailed=True), 0),
    (Parrot(type_of_parrot=ParrotType.NORWEGIAN_BLUE, number_of_coconuts=0, voltage=1.5, nailed=False), 18.0),
    (Parrot(type_of_parrot=ParrotType.NORWEGIAN_BLUE, number_of_coconuts=0, voltage=4, nailed=False), 24.0),
]


@pytest.mark.parametrize("parrot,expected_speed", test_cases)
def test_speed_of_parrot(parrot: Parrot, expected_speed: float) -> None:
    assert parrot.speed() == expected_speed
