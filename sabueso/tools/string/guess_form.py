from .pdb_text import string_is_pdb_text
from .pdb_id import string_is_pdb_id
from .uniprot_id import string_is_uniprot_id

def guess_form(string):

    output = None

    if string_is_pdb_text(string):
        output = 'string:pdb_text'
    elif string_is_pdb_id(string):
        output = 'string:pdb_id'
    elif string_is_uniprot_id(string):
        output = 'string:uniprot_id'

    return output

