import re
from parse.parse_input import parse_args_kwargs
from reactions import RateConstant

def parse_all_constants(constants_section:list):
    list_of_all_constants = []

    for constants_line in constants_section:
        constant = parse_constants_string(constants_line)
        list_of_all_constants.append(constant)

    return list_of_all_constants

def parse_constants_string(constants_str:str):
    args, kwargs = parse_args_kwargs(constants_str)
    
    name_str = args
    if 'k' in kwargs:
        kwargs['k'] = float(kwargs['k'])
    if 'f' in kwargs:
        kwargs['f'] = float(kwargs['f'])
    if 'A' in kwargs:
        kwargs['A'] = float(kwargs['A'])
    if 'E' in kwargs:
        kwargs['E'] = float(kwargs['E'])

    constant = RateConstant(name_str, **kwargs)
    return constant

def parse_reaction_constant(reaction_string):
    constant = RateConstant()
    return constant
    