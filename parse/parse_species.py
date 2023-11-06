from parse.parse_input import parse_args_kwargs
from species import Species, SpeciesType, EquivalentSpecies

def parse_all_species(species_section:list):
    list_of_all_species = []
    list_of_equivalent_species = []

    for species_line in species_section:

        species = parse_species_string(species_line)

        if isinstance(species, Species):
            list_of_all_species.append(species)
        elif isinstance(species, EquivalentSpecies):
            list_of_equivalent_species.append(species)

    return list_of_all_species, list_of_equivalent_species

def parse_species_string(species_str:str):

    # Split the line by whitespace and remove empty elements
    args, kwargs = parse_args_kwargs(species_str)

    # The line must have type and name
    assert(len(args) == 2)

    type_str = args[0]
    name_str = args[1]

    species_type = parse_species_type(type_str)

    if 'c0' in kwargs:
        kwargs['c0'] = float(kwargs['c0'])
    if 'FW' in kwargs:
        kwargs['FW'] = float(kwargs['FW'])

    try:
        species = Species(name_str, species_type, **kwargs)
        return species
    except:
        try:
            species = EquivalentSpecies(name_str, species_type, **kwargs)
            return species
        except:
            raise Exception('Not cool.')
    
def parse_species_type(type_str:str):

    if len(type_str) != 1:
        return None
    if type_str == 'U':
        return SpeciesType.UNIT
    elif type_str == 'P':
        return SpeciesType.POLY
    return None

