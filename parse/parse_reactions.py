import re
from reactions import ReactionSpecies, RateConstant, InitiatorDecompositionReaction, InitiationReaction, PropagationReaction, DepropagationReaction, TerminationCombinationReaction, TerminationDisproportionationReaction
from parse.parse_rate_constant import RateConstantParser
from typing import List

class ReactionParser:
    def __init__(self, species_list, equivalent_species_list, rate_constant_parser: RateConstantParser):
        self.species_list = species_list
        self.equivalent_species_list = equivalent_species_list
        self.rcp = rate_constant_parser
        
    # Address this function
    def parse_all_reactions(self, reactions_section:List[str]):
        
        list_of_all_reactions = []

        reactions_section = self.modify_reactions_section(reactions_section)

        for reaction_line in reactions_section:
            reaction_type, reactant_species, product_species, rate_constant = self.parse_reaction_string(reaction_line)
            reaction_object = self.create_reaction_object(reaction_type, reactant_species, product_species, rate_constant)

            for reaction in list_of_all_reactions:
                if reaction_object == reaction:
                    break
            else:
                list_of_all_reactions.append(reaction_object)

        return list_of_all_reactions

    def modify_reactions_section(self, reactions_section:List[str]):
        
        eq_species_present = True

        while eq_species_present:
            updated_reactions_section = []
            eq_species_present = False
            for reaction_line in reactions_section:
                for eq_species in self.equivalent_species_list:
                    if eq_species.name in reaction_line:
                        for sp in eq_species.eq:
                            new_reaction = reaction_line.replace(eq_species.name, sp, 1)
                            updated_reactions_section.append(new_reaction)
                        eq_species_present = True
                        break
                else:
                    updated_reactions_section.append(reaction_line)

            reactions_section = updated_reactions_section

        return updated_reactions_section

    def create_reaction_object(self, reaction_type, reactant_species, product_species, rate_constant):

        if (reaction_type == "ID"):
            reaction_object = InitiatorDecompositionReaction(rate_constant, reactant_species[0], product_species[0])
        elif (reaction_type == "IN"):
            reaction_object = InitiationReaction(rate_constant, reactant_species[0], reactant_species[1], product_species[0])
        elif (reaction_type == "PR"):
            reaction_object = PropagationReaction(rate_constant, reactant_species[1], reactant_species[0], product_species[0])
        elif (reaction_type == "DP"):
            reaction_object = DepropagationReaction(rate_constant, reactant_species[0], product_species[1], product_species[0])
        elif (reaction_type == "TC"):
            reaction_object = TerminationCombinationReaction(rate_constant, reactant_species[0], reactant_species[1], product_species[0])
        elif (reaction_type == "TD"):
            reaction_object = TerminationDisproportionationReaction(rate_constant, reactant_species[0], reactant_species[1], product_species[0])
        else:
            print("Invalid reaction type ", reaction_type)
            return None

        return reaction_object

    def parse_reaction_string(self, reaction_string:str) -> (List[ReactionSpecies], List[ReactionSpecies], RateConstant):
        
        reaction_type = reaction_string[:2]
        reaction_string = reaction_string[3:]
        # Split the reaction string into reactant and product sides
        reactant_side, product_side = re.split(r'\s*-\w*->\s*', reaction_string)

        # Parse the reactant side
        reactants = re.split(r'\s*\+\s*', reactant_side)
        reactant_species = [self.parse_reaction_species_string(reactant) for reactant in reactants]

        # Parse the product side
        products = re.split(r'\s*\+\s*', product_side)
        product_species = [self.parse_reaction_species_string(product) for product in products]

        #Call parse_rate_constant
        rate_constant = self.rcp.parse_reaction_constant(reaction_string)

        return reaction_type, reactant_species, product_species, rate_constant
        
    def parse_reaction_species_string(self, reaction_species_string:str) -> ReactionSpecies:
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
        for s in self.species_list:
            if (name == s.name):
                species = ReactionSpecies(s, coeff)
                return species

        species = ReactionSpecies(None, coeff)
        return species

    # Create additional reactions for equivalent species