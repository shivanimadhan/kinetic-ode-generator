
from dataclasses import dataclass
from typing import List, Dict
import math
from typing import List, Dict

from species import Species

class RateConstant:
    def __init__(self, name, **kwargs):
        self.name = name
        self.parameters = kwargs

    def get_k(self, temperature=None):
        raise NotImplementedError("Subclasses must implement the get_k method")
    
    def __repr__(self):
        return f'{self.name}, {self.parameters}'

class ConstantRateConstant(RateConstant):
    def __init__(self, name, k, **kwargs):
        super().__init__(name, **kwargs)
        self.k = k

    def get_k(self, T:float):
        return self.k

class ArrheniusRateConstant(RateConstant):
    def __init__(self, name, A, E, **kwargs):
        super().__init__(name, **kwargs)
        self.A = A
        self.E = E

    def get_k(self, T:float):
        return self.A * math.exp(-self.E / (8.314 * T))

@dataclass
class ReactionSpecies:
    #name:str
    species:Species
    coeff:int

<<<<<<< HEAD
=======

from dataclasses import dataclass
import math
from typing import List, Dict

from species import Species

class RateConstant:
    def __init__(self, name, **kwargs):
        self.name = name
        self.parameters = kwargs

    def get_k(self, temperature=None):
        raise NotImplementedError("Subclasses must implement the get_k method")

class ConstantRateConstant(RateConstant):
    def __init__(self, name, k, **kwargs):
        super().__init__(name, **kwargs)
        self.k = k

    def get_k(self, T:float):
        return self.k

class ArrheniusRateConstant(RateConstant):
    def __init__(self, name, A, E, **kwargs):
        super().__init__(name, **kwargs)
        self.A = A
        self.E = E

    def get_k(self, T:float):
        return self.A * math.exp(-self.E / (8.314 * T))


@dataclass
class ReactionSpecies:
    name:str
    species:Species
    coeff:int

>>>>>>> 82fc88d95cd345c73a027c3de27ca8bf2373795d
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
        rate = self.rate_constant.get_k()
        for reactant_species in self.reactant_species:
            rate *= reactant_species.coeff * (c[reactant_species.name] ** reactant_species.coeff)
        return rate
    
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
<<<<<<< HEAD
        )

    def __init__(self, rate_constant: RateConstant,
        poly_reactant1, poly_reactant2, poly_product1, poly_product2):
        super().__init__(rate_constant, 0, 2, 0, 2)

        self.poly_reactants[0] = poly_reactant1
        self.poly_reactants[1] = poly_reactant2 

        self.poly_products[0] = poly_product1
        self.poly_products[1] = poly_product2

    def calculate_rate(self, c:dict):

        return self.rate_constant.get_k() * c[self.poly_reactants[0]] * c[self.poly_products[1]]      
=======
        )
>>>>>>> 82fc88d95cd345c73a027c3de27ca8bf2373795d
