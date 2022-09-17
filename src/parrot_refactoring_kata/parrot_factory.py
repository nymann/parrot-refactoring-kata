from enum import Enum
from typing import Type

from parrot_refactoring_kata.parrot import Parrot
from parrot_refactoring_kata.parrots.african import AfricanParrot
from parrot_refactoring_kata.parrots.european import EuropeanParrot
from parrot_refactoring_kata.parrots.norwegian_blue import NorwegianBlueParrot


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class ParrotFactory:
    _register: dict[ParrotType, Type[Parrot]] = {
        ParrotType.EUROPEAN: EuropeanParrot,
        ParrotType.AFRICAN: AfricanParrot,
        ParrotType.NORWEGIAN_BLUE: NorwegianBlueParrot,
    }

    @classmethod
    def create(
        cls,
        type_of_parrot: ParrotType,
        number_of_coconuts: int,
        voltage: int | float,
        nailed: bool,
    ):
        if type_of_parrot not in cls._register:
            raise KeyError("We don't support that parrot type yet")
        return cls._register[type_of_parrot](
            number_of_coconuts=number_of_coconuts,
            voltage=voltage,
            nailed=nailed,
        )
