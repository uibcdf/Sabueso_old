def guess_form(string):

    from sabueso.tools.string.pdb import string_is_pdb
    from sabueso.tools.string.pdbid import string_is_pdbid

    output = None

    if string_is_pdb(string):
        output = 'string:pdb'
    elif string_is_pdbid(string):
        output = 'string:pdbid'

    return output

