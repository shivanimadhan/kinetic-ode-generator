from dataclasses import dataclass
from enum import Enum
from typing import List

class SpeciesType(Enum):
    UNIT = 1
    POLY = 2

@dataclass(frozen=True)
class Species:
    name:str
    type:SpeciesType
    FW:float=1.
    c0:float=0.

    def __str__(self):
        return self.name

@dataclass
class EquivalentSpecies:
    name:str
    type:SpeciesType
    eq:List[str]

    # def __init__(self, name:str, type:SpeciesType, eq:str):
    #     self.name = name
    #     self.type = type
    #     self.eq = eq
    #     parts = eq.split('|')
    #     print(parts)
    # and_spec:list
    # or_spec:list