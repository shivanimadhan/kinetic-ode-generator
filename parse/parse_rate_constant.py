import re
from parse.parse_input import parse_args_kwargs
from reactions import RateConstant

class RateConstantParser:

    # all_constants = []
    
    def __init__(self):
        self.all_constants = []

    def parse_all_constants(self, constants_section:list):
        for constants_line in constants_section:
            constant = self.parse_constants_string(constants_line)
            self.all_constants.append(constant)

    def parse_constants_string(self, constants_str:str):
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

    def parse_reaction_constant(self, reaction_string):
        name = re.compile(r'-(\w+)->')
        match = name.search(reaction_string)

        for c in self.all_constants:
            if (match.group(1) == c.name[0]):
                return c

        