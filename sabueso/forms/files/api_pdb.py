form_name='file:pdb'

is_form = {
        'file:pdb': form_name
    }

def get_cards(molecular_system):

    from sabueso.tools.file.pdb import parse

    pdb = parse(molecular_system)

    pass

