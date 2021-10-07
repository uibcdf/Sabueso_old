from .forms import dict_get_cards

def get_cards(molecular_system, entities='all'):

    from sabueso import get_form

    form = get_form(molecular_system)

    output = dict_get_cards[form](molecular_system, indices='all')

    return output

