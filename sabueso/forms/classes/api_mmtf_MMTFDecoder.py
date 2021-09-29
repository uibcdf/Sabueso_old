from mmtf import MMTFDecoder as _mmtf_MMTFDecoder

form_name='mmtf.MMTFDecoder'

is_form={
    _mmtf_MMTFDecoder : form_name,
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

    raise NotImplementedError()

def get_entity_name(item, indices='all'):

    raise NotImplementedError()

def get_entity_id(item, indices='all'):

    raise NotImplementedError()

def get_entity_type(item, indices='all'):

    raise NotImplementedError()

def get_n_entities(item, indices='all'):

    raise NotImplementedError()

def is_ion(item, indices='all'):

    raise NotImplementedError()

def is_water(item, indices='all'):

    raise NotImplementedError()

def is_cosolute(item, indices='all'):

    raise NotImplementedError()

def is_small_molecule(item, indices='all'):

    raise NotImplementedError()

def is_lipid(item, indices='all'):

    raise NotImplementedError()

def is_peptide(item, indices='all'):

    raise NotImplementedError()

def is_protein(item, indices='all'):

    raise NotImplementedError()

def is_rna(item, indices='all'):

    raise NotImplementedError()

def is_dna(item, indices='all'):

    raise NotImplementedError()

