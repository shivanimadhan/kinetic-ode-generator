from reactions import ReactionSpecies, RateConstant, Reaction, InitiatorDecompositionReaction, InitiationReaction, PropagationReaction, DepropagationReaction, TerminationCombinationReaction, TerminationDisproportionationReaction
from species import Species, SpeciesType, EquivalentSpecies
from parse.parse_reactions import ReactionParser
from typing import List, Dict
import numpy as np

def kinetic_odes(t: List[int], c: Dict[str, float], reactions_list: List[Reaction]):
    dcdt = np.zeros(len(c))

    for i, key in enumerate(c):
        for reaction in reactions_list:
            if reaction.is_species_present("reactant", key):
                print("key for reactant", key)
                dcdt[i] -= reaction.calculate_rate(c)
                print("dcdt[i] for reactant:", dcdt[i])

            if reaction.is_species_present("product", key):
                print("key for product", key)
                dcdt[i] += reaction.calculate_rate(c)
                print("dcdt[i] for product:", dcdt[i])
        
        print("end of species")
    
    #print(f't = {t}, c = {c}, dcdt = {dcdt}')

    return dcdt