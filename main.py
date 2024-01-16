from parse.parse_reactions import ReactionParser
from parse.parse_species import parse_all_species
from parse.parse_rate_constant import RateConstantParser
from parse.parse_input import separate_input_file
from create_diff_eqs import write_kinetic_odes
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sys

def write_odes(input_file):
    sections = separate_input_file(input_file)

    species_section = sections['species']
    all_species, all_equivalent_species = parse_all_species(species_section)

    constants_section = sections['rate constants']
    rcp = RateConstantParser()
    all_constants = rcp.parse_all_constants(constants_section)

    reactions_section = sections['reactions']
    rp = ReactionParser(all_species, all_equivalent_species, rcp)
    all_reactions = rp.parse_all_reactions(reactions_section)

    write_kinetic_odes(all_species, all_reactions, all_constants)