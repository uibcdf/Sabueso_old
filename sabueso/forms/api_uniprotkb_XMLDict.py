form_name='uniprotkb.XMLDict'

is_form={
}

def this_dict_is_a_uniprotkb_XMLDict(item):

    return list(item.keys())==['uniprot']

###### Get

def get_entity_index(item, indices='all'):

    return [0]

def get_entity_name(item, indices='all'):

    from sabueso.tools.uniprotkb_XMLDict import get_entity_name as _get

    output = []

    entity_name = _get(item, entity=indices)

    return output

def get_entity_id(item, indices='all'):

    accession = item['uniprot']['entry']['accession'][0]

    return [accession]

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

