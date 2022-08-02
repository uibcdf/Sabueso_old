from sabueso.tools.string_pdb_text import is_pdb_text
from sabueso.tools.string_pdb_id import is_pdb_id
from sabueso.tools.string_uniprot_id import is_uniprot_id

def guess_form(string):

    output = None

    if is_pdb_text(string):
        output = 'string:pdb_text'
    elif is_pdb_id(string):
        output = 'string:pdb_id'
    elif is_uniprot_id(string):
        output = 'string:uniprot_id'

    return output

