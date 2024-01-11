# Functions to parse the full input file
# - Parse general input parameters
# - - Reaction temperature
# - - Reaction type
# - - Reaction time (s)
# - Parse species
# - - Type
# - - Name
# - - FW
# - - c0
# - parse rate constants
# - parse 

import re
from typing import Dict, List

VALID_SECTION_HEADERS = ['general', 'species', 'rate constants', 'reactions']
IGNORE_STRINGS = ['#', '/']

# Check if a line is empty or commented out
def can_ignore(line:str)->bool:
    """Check if a line is empty or commented out

    Args:
        line (str): line in the input file

    Returns:
        bool: True if the line can be ignored, else False
    """

    line = line.strip()

    if line == '':
        return True
    
    for ignore_str in IGNORE_STRINGS:
        if line.startswith(ignore_str):
            return True
    return False

def is_section_header(line:str)->bool:
    if re.match(r'^\s', line) or is_section_end(line):
        return False
    return True

def is_section_end(line:str)->bool:
    if line.startswith('end'):
        return True
    return False

def parse_args_kwargs(line:str)->(List[str], Dict[str, str]):
    """Separate the args and kwargs in the input file

    Args:
        line (str): line in the input file

    Returns:
        (List[str], Dict[str, str]): tuple of args and kwargs in input file
    """

    # Split the input string by spaces to get individual parts
    parts = line.split()

    # Initialize lists to store arguments and kwargs
    args = []
    kwargs = {}

    # Iterate through the parts
    for part in parts:
        if '=' in part:
            # Split the part into key and value using '='
            key, value = part.split('=')
            kwargs[key] = value
        else:
            args.append(part)

    return args, kwargs

def separate_input_file(input_filepath:str)->Dict[str, List[str]]:
    """_summary_

    Args:
        input_filepath (str): _description_

    Raises:
        Exception: _description_

    Returns:
        Dict[str, List[str]]: dictionary with section headers as keys 
            and a list of lines within the section as values
    """

    sections = {section_header: [] for section_header in VALID_SECTION_HEADERS}
    #print(sections)

    with open(input_filepath, 'r') as file:

        current_section_header = None
        current_section_lines = []

        for line in file:

            if can_ignore(line):
                continue
            elif is_section_end(line):

                sections[current_section_header] = current_section_lines
                current_section_lines = []

            elif is_section_header(line):
                current_section_header = line.strip()

                # Add into section header func instead of leaving it here
                if current_section_header not in VALID_SECTION_HEADERS:
                    raise Exception(f'\'{current_section_header}\' is not a valid section header. Valid section headers are {VALID_SECTION_HEADERS}')

            else:
                line = line.strip()
                current_section_lines.append(line)

    return sections
            
