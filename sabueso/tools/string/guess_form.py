from .pdb import string_is_pdb
from .pdbid import string_is_pdbid
from .uniprot import string_is_uniprot

def guess_form(string):

    output = None

    if string_is_pdb(string):
        output = 'string:pdb'
    elif string_is_pdbid(string):
        output = 'string:pdbid'
    elif string_is_uniprot(string):
        output = 'string:uniprot'

    return output


