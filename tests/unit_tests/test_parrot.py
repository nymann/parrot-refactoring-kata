from dataclasses import dataclass

import pytest

from parrot_refactoring_kata.parrot import Parrot
from parrot_refactoring_kata.parrot_factory import ParrotFactory
from parrot_refactoring_kata.parrot_factory import ParrotType


@dataclass
class TestCase:
    __test__ = False

    parrot_type: ParrotType
    number_of_coconuts: int = 0
    voltage: float = 0
    nailed: bool = False
    expected: float = 0

    @property
    def parrot(self) -> Parrot:
        return ParrotFactory.create(
            parrot_type=self.parrot_type,
            number_of_coconuts=self.number_of_coconuts,
            voltage=self.voltage,
            nailed=self.nailed,
        )

    @property
    def actual(self) -> float:
        return self.parrot.speed()


test_cases = [
    TestCase(parrot_type=ParrotType.EUROPEAN, expected=12.0),
    TestCase(parrot_type=ParrotType.AFRICAN, number_of_coconuts=1, expected=3.0),
    TestCase(parrot_type=ParrotType.AFRICAN, number_of_coconuts=2),
    TestCase(parrot_type=ParrotType.AFRICAN, expected=12.0),
    TestCase(parrot_type=ParrotType.NORWEGIAN_BLUE, voltage=1.5, nailed=True),
    TestCase(parrot_type=ParrotType.NORWEGIAN_BLUE, voltage=1.5, expected=18.0),
    TestCase(parrot_type=ParrotType.NORWEGIAN_BLUE, voltage=4, expected=24.0),
]


@pytest.mark.parametrize("test_case", test_cases)
def test_speed_of_parrot(test_case: TestCase) -> None:
    assert test_case.expected == test_case.actual
