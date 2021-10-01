from sabueso.tools.string_pdb_text import string_is_pdb_text
from sabueso.tools.string_pdb import string_is_pdb
from sabueso.tools.string_uniprot import string_is_uniprot

def guess_form(string):

    output = None

    if string_is_pdb_text(string):
        output = 'string:pdb_text'
    elif string_is_pdb(string):
        output = 'string:pdb'
    elif string_is_uniprot(string):
        output = 'string:uniprot'

    return output

