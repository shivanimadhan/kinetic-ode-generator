
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

class Reaction:

#     def __init__(self, rate_constant: RateConstant,
#             num_unit_reactants:int, num_poly_reactants:int,
#             num_unit_products:int,  num_poly_products:int):
#         self.rate_constant = rate_constant

#         self.unit_reactant_species = [] * num_unit_reactants
#         self.poly_reactant_species = [] * num_poly_reactants
        
#         self.unit_product_species = [] * num_unit_products
#         self.poly_product_species = [] * num_poly_products

#     def clean(self):

#         self.reactant_species = self.unit_reactant_species + self.poly_reactant_species
#         self.product_species = self.unit_product_species + self.poly_product_species
#         self.all_species = self.reactant_species + self.product_species

#     def calculate_rate(self, c):

#         # Assumes elementary reactions
#         rate = self.rate_constant
#         for reactant_species in self.reactant_species:
#             rate *= reactant_species.coeff * (c[reactant_species.name] ** reactant_species.coeff)
#         return rate
    
#     # def get_rate_string(self):
#     #     rate_strings = [self.rate_constant]
#     #     for reactant_species in self.reactant_species:
#     #         rate_strings.append(f'{reactant_species.coeff}*{c[reactant_species.name]}**{reactant_species.coeff}')
#     #     rate_string = rate_strings.join('*')
#     #     return rate_string
            
# class InitiatorDecompositionReaction(Reaction):

#     def __init__(self, rate_constant: RateConstant, 
#         unit_reactant, unit_product):
#         super().__init__(rate_constant, 1, 0, 2, 0)

#         self.unit_reactants[0] = unit_reactant
#         self.unit_products[0]  = unit_product
#         self.unit_products[1]  = unit_product

#     def calculate_rate(self, c:dict):

#         return self.rate_constant.get_k() * c[self.unit_reactants[0]]
    
# class PropagationReaction(Reaction):

#     def __init__(self, rate_constant: RateConstant,
#         unit_reactant, poly_reactant, poly_product):
#         super().__init__(rate_constant, 1, 1, 0, 1)

#         self.unit_reactants[0] = unit_reactant
#         self.poly_reactants[0] = poly_reactant
#         self.poly_products[0]  = poly_product

#     def calculate_rate(self, c:dict):

#         return self.rate_constant.get_k() * c[self.unit_reactants[0]] * c[self.poly_reactants[0]]

# class TerminationCombinationReaction(Reaction):

#     def __init__(self, rate_constant: RateConstant,
#         poly_reactant1, poly_reactant2, poly_product):
#         super().__init__(rate_constant, 0, 2, 0, 1)

#         self.poly_reactants[0] = poly_reactant1
#         self.poly_reactants[1] = poly_reactant2

#         self.poly_products[0] = poly_product

#     def calculate_rate(self, c:dict):

#         return self.rate_constant.get_k() * c[self.poly_reactants[0]] * c[self.poly_reactants[1]]

# class TerminationDisproportionationReaction(Reaction):

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
