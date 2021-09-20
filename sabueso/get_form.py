from .get_cards_from import dict_get_cards_from
from .get_cards_from import dict_is_form
from sabueso._private_tools.lists_and_tuples import is_list_or_tuple
from sabueso.tools.molecular_system import is_file, is_string

def get_form(molecular_system):

    if type(molecular_system)==str:
        file_form = is_file(molecular_system)
        if file_form:
            return dict_is_form[file_form]
        string_form = is_string(molecular_system)
        if string_form:
            return dict_is_form[string_form]

    if is_list_or_tuple(molecular_system):
        output = [get_form(ii) for ii in molecular_system]
        return output

    try:
        return dict_is_form[type(molecular_system)]
    except:
        try:
            return dict_is_form[molecular_system]
        except:
            raise NotImplementedError()



    form = get_form(molecular_system)
    output = dict_get_cards_from[form](molecular_system)

    return output

