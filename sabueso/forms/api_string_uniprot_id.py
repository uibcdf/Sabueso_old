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

def is_ion(item, indices='all'):

    return [False]

def is_water(item, indices='all'):

    return [False]

def is_cosolute(item, indices='all'):

    return [False]

def is_small_molecule(item, indices='all'):

    return [False]

def is_lipid(item, indices='all'):

    return [False]

def is_peptide(item, indices='all'):

    return [False]

def is_protein(item, indices='all'):

    return [True]

def is_rna(item, indices='all'):

    return [False]

def is_dna(item, indices='all'):

    return [False]

