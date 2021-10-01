from sabueso.forms import dict_is_form
from sabueso._private_tools.lists_and_tuples import is_list_or_tuple
from sabueso._private_tools.molecular_system import is_file, is_string
from collections import OrderedDict

def get_form(molecular_system):

    if type(molecular_system)==str:

        file_form = is_file(molecular_system)
        if file_form:
            return dict_is_form[file_form]
        string_form = is_string(molecular_system)
        if string_form:
            return dict_is_form[string_form]

    if type(molecular_system)==dict:

        raise NotImplementedError()

    if type(molecular_system)==OrderedDict:

        from sabueso.forms.classes.api_uniprotkb_XMLDict import this_dict_is_uniprotkb_XMLDict
        from sabueso.forms.classes.api_uniprotkb_XMLDict import form as form_uniprotkb_XMLDict

        if this_dict_is_uniprotkb_XMLDict(molecular_system):
            return form_uniprotkb_XMLDict
        else:
            raise NotImplementedError()

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

