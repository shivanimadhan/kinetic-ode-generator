from dataclasses import dataclass
from typing import List, Dict
from collections import Counter
import math
from typing import List, Dict

from species import Species

class RateConstant:
    def __init__(self, name, **kwargs):
        self.name = name
        self.parameters = kwargs

    def get_k(self):
        return 0.0
    
    def __repr__(self):
        return f'{self.name}, {self.parameters}'

class ConstantRateConstant(RateConstant):
    def __init__(self, name, k, **kwargs):
        super().__init__(name, **kwargs)
        self.k = k

    def get_k(self):
        return self.k

class ArrheniusRateConstant(RateConstant):
    def __init__(self, name, A, E, **kwargs):
        super().__init__(name, **kwargs)
        self.A = A
        self.E = E

    def get_k(self, T: float):
        return self.A * math.exp(-self.E / (8.314 * T))

@dataclass(frozen=True)
class ReactionSpecies:
    species:Species
    coeff:int

class Reaction:
    def __init__(self, rate_constant: RateConstant,
                 unit_reactant_species:List[ReactionSpecies], poly_reactant_species:List[ReactionSpecies],
                 unit_product_species:List[ReactionSpecies], poly_product_species:List[ReactionSpecies]):
        self.rate_constant = rate_constant

        self.unit_reactant_species = unit_reactant_species
        self.poly_reactant_species = poly_reactant_species
        self.unit_product_species = unit_product_species
        self.poly_product_species = poly_product_species

        self.reactant_species = self.unit_reactant_species + self.poly_reactant_species
        self.product_species = self.unit_product_species + self.poly_product_species
        self.all_species = self.reactant_species + self.product_species

    def calculate_rate(self, c: Dict[str, float]) -> float:
        # Assumes elementary reactions
        rate = self.rate_constant.get_k(273.15)
        #print("rate 1:", rate)
        for rs in self.reactant_species:
            #print ("other part:", (c[rs.species.name] ** rs.coeff))
            rate *= rs.coeff * (c[rs.species.name] ** rs.coeff)
        #print("rate 2:", rate)
        return rate
    
    def get_rate_string(self, all_species: List[Species]) -> float:
        # Assumes elementary reactions
        rate_string_list = [self.rate_constant.name]
        #print(all_species)

        for rs in self.reactant_species:
            for i, s in enumerate(all_species):
                #print(s.name)
                if (rs.species.name == s.name):
                    rate_string_list.append(f'c[{i}]')

        rate_string = "*".join(rate_string_list)
        return rate_string
        #return rate_string_list

        # rate = self.rate_constant.get_k(273.15)
        # print("rate 1:", rate)
        # for rs in self.reactant_species:
        #     print ("other part:", (c[rs.species.name] ** rs.coeff))
        #     rate *= rs.coeff * (c[rs.species.name] ** rs.coeff)
        # print("rate 2:", rate)
        # return rate
    
    def is_species_present(self, species_type: str, species_name: str) -> bool:
        if species_type == "reactant":
            return species_name in [s.species.name for s in self.reactant_species]
        
        if species_type == "product":
            return species_name in [s.species.name for s in self.product_species]
        
        return False

    def __repr__(self):
        return f'Rate Constant:{self.rate_constant},\nUnit Reactant Species: {self.unit_reactant_species},\nPoly Reactant Species: {self.poly_reactant_species},\nUnit Product Species: {self.unit_product_species},\nPoly Product Species: {self.poly_product_species}\n\n'
    
    def __eq__(self, other):
        return (Counter(self.reactant_species) == Counter(other.reactant_species)) and (Counter(self.product_species) == Counter(other.product_species))

class InitiatorDecompositionReaction(Reaction):

    def __init__(self, rate_constant: RateConstant, 
                 unit_reactant: ReactionSpecies, 
                 unit_product: ReactionSpecies):
        super().__init__(
            rate_constant=rate_constant, 
            unit_reactant_species=[unit_reactant], 
            poly_reactant_species=[],
            unit_product_species=[unit_product],
            poly_product_species=[]
        )

class InitiationReaction(Reaction):

    def __init__(self, rate_constant: RateConstant,
                 unit_reactant1: ReactionSpecies, unit_reactant2: ReactionSpecies, 
                 poly_product: ReactionSpecies):
        super().__init__(
            rate_constant=rate_constant,
            unit_reactant_species=[unit_reactant1, unit_reactant2],
            poly_reactant_species=[],
            unit_product_species=[],
            poly_product_species=[poly_product]
        )

class PropagationReaction(Reaction):

    def __init__(self, rate_constant: RateConstant,
                 unit_reactant: ReactionSpecies, poly_reactant: ReactionSpecies, 
                 poly_product: ReactionSpecies):
        super().__init__(
            rate_constant=rate_constant,
            unit_reactant_species=[unit_reactant],
            poly_reactant_species=[poly_reactant],
            unit_product_species=[],
            poly_product_species=[poly_product]
        )

class DepropagationReaction(Reaction):

    def __init__(self, rate_constant: RateConstant,
                 poly_reactant: ReactionSpecies, unit_product: ReactionSpecies, 
                 poly_product: ReactionSpecies):
        super().__init__(
            rate_constant=rate_constant,
            unit_reactant_species=[],
            poly_reactant_species=[poly_reactant],
            unit_product_species=[unit_product],
            poly_product_species=[poly_product]
        )

class TerminationCombinationReaction(Reaction):

    def __init__(self, rate_constant: RateConstant,
                 poly_reactant1: ReactionSpecies, poly_reactant2: ReactionSpecies, 
                 poly_product: ReactionSpecies):
        super().__init__(
            rate_constant=rate_constant,
            unit_reactant_species=[],
            poly_reactant_species=[poly_reactant1, poly_reactant2],
            unit_product_species=[],
            poly_product_species=[poly_product]
        )

class TerminationDisproportionationReaction(Reaction):

    def __init__(self, rate_constant: RateConstant,
                 poly_reactant1: ReactionSpecies, poly_reactant2: ReactionSpecies, 
                 poly_product: ReactionSpecies):
        super().__init__(
            rate_constant=rate_constant,
            unit_reactant_species=[],
            poly_reactant_species=[poly_reactant1, poly_reactant2],
            unit_product_species=[],
            poly_product_species=[poly_product]
        )