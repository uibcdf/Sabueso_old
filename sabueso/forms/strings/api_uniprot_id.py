import sys
import importlib

form_name='string:uniprot_id'

is_form = {
    'string:uniprot_id': form_name,
    }



###### Get

def aux_get(item, indices='all', frame_indices='all'):

    from sabueso.tools.string.uniprot_id.to_uniprotkb_XMLDict import to_uniprotkb_XMLDict

    method_name = sys._getframe(1).f_code.co_name

    tmp_item = to_uniprotkb_XMLDict(item)
    module = importlib.import_module('sabueso.forms.classes.api_uniprotkb_XMLDict')
    _get = getattr(module, method_name)
    output = _get(tmp_item, indices=indices)

    return output


def get_entity_index(item, indices='all'):

    return [0]

def get_entity_name(item, indices='all'):

    return aux_get(item, indices=indices)

def get_entity_id(item, indices='all'):

    return [0]

def get_entity_type(item, indices='all'):

    return ['protein']

def get_n_entities(item, indices='all'):

    return 1

