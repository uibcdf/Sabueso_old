from sabueso.get_form import get_form
from sabueso.forms import dict_get_entity_name

def get_entity_name(molecular_system):

    form = get_form(molecular_system)
    output = dict_get_entity_name[form](molecular_system)
    return output


