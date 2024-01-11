from reactions import ReactionSpecies, RateConstant, Reaction, InitiatorDecompositionReaction, InitiationReaction, PropagationReaction, DepropagationReaction, TerminationCombinationReaction, TerminationDisproportionationReaction
from species import Species, SpeciesType, EquivalentSpecies
from parse.parse_reactions import ReactionParser
from typing import List, Dict
import numpy as np

def write_kinetic_odes(species_list: List[Species], reactions_list: List[Reaction], rate_constants_list: List[RateConstant]):
    dcdt = np.zeros_like(species_list)

    for i, key in enumerate(species_list):
        temp_list = []
        for reaction in reactions_list:
            if reaction.is_species_present("reactant", key.name):
                temp_list.append(f"-{reaction.get_rate_string(species_list)}")

            if reaction.is_species_present("product", key.name):
                temp_list.append(f"{reaction.get_rate_string(species_list)}")

        dcdt[i] = " + ".join(temp_list)

    c0 = extract_initial_conc(species_list)    
    write_to_file(c0, dcdt, rate_constants_list)

def extract_initial_conc(species_list: List[Species]):
    return [species.c0 for species in species_list]

def write_to_file(c0: List[float], dcdt: List[str], rate_constants_list: List[RateConstant], output_file="kinetic_odes.py"):
    with open(output_file, 'w') as file:
        file.write("import numpy as np\n\n")

        file.write(f"c0 = {c0}\n\n")

        file.write(f"def kinetic_odes(t, c):\n")

        for value in rate_constants_list:
            file.write(f"\t{value.name} = {value.get_k()}\n")

        file.write("\n\tdcdt = np.zeros_like(c)\n\n")

        for i, value in enumerate(dcdt):
            file.write(f"\tdcdt[{i}] = {value}\n")

        file.write("\n\treturn dcdt")    