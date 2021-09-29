
def is_protein(molecular_system, indices='all'):

    from sabueso import get_form
    from sabueso.forms import dict_is_protein

    form = get_form(molecular_system)

    return dict_is_protein[form](molecular_system, indices='all')

