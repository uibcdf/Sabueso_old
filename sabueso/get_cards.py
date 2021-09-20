from .get_form import get_form
from .get_cards_from import dict_get_cards_from

def get_cards(molecular_system, molecule_index='all'):

    form = get_form(molecular_system)
    output = dict_get_cards_from[form](molecular_system)

    return output

