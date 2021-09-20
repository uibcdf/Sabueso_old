from .pdb import string_is_pdb
from .pdbid import string_is_pdbid

def guess_form(string):

    output = None

    if string_is_pdb(string):
        output = 'string:pdb'
    elif string_is_pdbid(string):
        output = 'string:pdbid'

    return output


