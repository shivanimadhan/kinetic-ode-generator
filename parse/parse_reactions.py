
import re
from reactions import ReactionSpecies

def parse_all_reactions():
    return

def parse_reaction_string(reaction_string):
    # Split the reaction string into reactant and product sides
    reactant_side, product_side = re.split(r'\s*-\w*->\s*', reaction_string)

    # Parse the reactant side
    reactants = re.split(r'\s*\+\s*', reactant_side)
    reactant_species = [parse_reaction_species_string(species) for species in reactants]

    # Parse the product side
    products = re.split(r'\s*\+\s*', product_side)
    product_species = [parse_reaction_species_string(species) for species in products]

    return reactant_species, product_species

def parse_reaction_species_string(reaction_species_string):
    # Define a regular expression pattern to match the number and the rest of the string
    pattern = r'^(\d*)(.*)$'

    # Use re.match() to find the match at the beginning of the string
    match = re.match(pattern, reaction_species_string)

    if match:
        number_part = match.group(1)
        remaining_part = match.group(2)
        if number_part:
            number = int(number_part)
        else:
            number = 1

        print("Number:", number)
        print("Remaining Part:", remaining_part)
    else:
        print("No match found.")
    
    species = ReactionSpecies(remaining_part, None, number)
    return species
