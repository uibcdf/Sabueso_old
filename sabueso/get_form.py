from sabueso.forms import dict_is_form, file_extensions_recognized, string_names_recognized
from sabueso._private_tools.lists_and_tuples import is_list_or_tuple
from collections import OrderedDict

def get_form(item):

    if is_list_or_tuple(item):

        output = [get_form_name(ii) for ii in item]
        return output

    try:

        return dict_is_form[type(item)]

    except:

        try:

            return dict_is_form[item]

        except:

            if type(item)==str:

                file_extension = item.split('.')[-1].lower()
                if file_extension in file_extensions_recognized:
                    return 'file:'+file_extension

                if ':' in item:
                    string_name = item.split(':')[0]
                    if string_name in string_names_recognized:
                        return 'string:'+string_name

                else:

                    from sabueso.tools.string_uniprot_id import is_string_uniprot_id
                    from sabueso.tools.string_pdb_id import is_string_pdb_id
                    from sabueso.tools.string_pdb_text import is_string_pdb_text
                    from sabueso.tools.string_entity_name import is_string_entity_name
                    from sabueso.tools.string_entity_query import is_string_entity_query

                    if is_string_uniprot_id(item):
                        return 'string:uniprot_id'
                    elif is_string_pdb_id(item):
                        return 'string:pdb_id'
                    elif is_string_pdb_text(item):
                        return 'string:pdb_text'
                    elif is_string_entity_name(item):
                        return 'string:entity_name'
                    elif is_string_entity_query(item):
                        return 'string:entity_query'
                    else:
                        raise NotImplementedError()

            elif type(item)==dict:

                from sabueso.tools.sabueso_ProteinDict import is_sabueso_ProteinDict
                from sabueso.forms.classes.api_sabueso_ProteinDict import form_name as form_name_sabueso_ProteinDict

                if is_sabueso_ProteinDict:
                    return form_name_sabueso_ProteinDict

                raise NotImplementedError()

            elif type(item)==OrderedDict:

                from sabueso.tools.sabueso_UniProtKB_XMLDict import is_sabueso_UniProtKB_XMLDict
                from sabueso.forms.classes.api_sabueso_UniProtKB_XMLDict import form_name as form_name_sabueso_UniProtKB_XMLDict

                if is_sabueso_UniProtKB_XMLDict(item):
                    return form_name_sabueso_UniProtKB_XMLDict
                else:
                    raise NotImplementedError()

            else:

                raise NotImplementedError()

