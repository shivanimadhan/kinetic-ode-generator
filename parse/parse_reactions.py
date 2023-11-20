import re
from reactions import ReactionSpecies
from parse.parse_rate_constant import RateConstantParser
from typing import List

class ReactionParser:
    def __init__(self, species_list):
        self.all_species = species_list
    # Address this function
    def parse_all_reactions(reactions_section:List[str]):
        return

    def parse_reaction_string(reaction_string):
        # Parse reaction type

        # Split the reaction string into reactant and product sides
        reactant_side, product_side = re.split(r'\s*-\w*->\s*', reaction_string)

        # Parse the reactant side
        # What happens if there's only one reactant? 
        reactants = re.split(r'\s*\+\s*', reactant_side)
        reactant_species = [ReactionParser.parse_reaction_species_string(reactant) for reactant in reactants]

        # Parse the product side
        products = re.split(r'\s*\+\s*', product_side)
        product_species = [ReactionParser.parse_reaction_species_string(product) for product in products]

        #Call parse_rate_constant
        rate_constant = RateConstantParser.parse_reaction_constant(reaction_string)

        return reactant_species, product_species, rate_constant
    # Address this function
    def parse_reaction_species_string(reaction_species_string):
        # Define a regular expression pattern to match the number and the rest of the string
        pattern = r'^(\d*)(.*)$'

        # Use re.match() to find the match at the beginning of the string
        match = re.match(pattern, reaction_species_string)

        if match:
            coeff_part = match.group(1)
            name = match.group(2)
            if coeff_part:
                coeff = int(coeff_part)
            else:
                coeff = 1

        # Match the name with the species
        for s in all_species:
            if (name == s.name):
                species = ReactionSpecies(s, coeff)
                return species

        species = ReactionSpecies(None, coeff)
        return species

    # Create additional reactions for equivalent species