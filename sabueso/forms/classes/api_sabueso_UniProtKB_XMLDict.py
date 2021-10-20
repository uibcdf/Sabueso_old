form_name='sabueso.UniProtKB_XMLDict'

is_form={
}

def this_dict_is_a_sabueso_UniProtKB_XMLDict(item):

    from sabueso.tools.sabueso_UniProtKB_XMLDict import is_sabueso_UniProtKB_XMLDict

    return is_UniProtKB_XMLDict(item)

def to_string_ec_id(item, indices='all'):

    from sabueso.tools.sabueso_UniProtKB_XMLDict.get_ec import get_ec

    ec = get_ec(item, entity=entity)

    output = 'ec:'+ec.value

    return output

def to_string_uniprot_id(item, entity='all'):

    from sabueso.tools.sabueso_UniProtKB_XMLDict import get_uniprot_id

    uniprot = get_uniprot(item, entity=entity)

    output = 'uniprot:'+uniprot.value

    return output

###### Get

def get_entity_index(item, indices='all'):

    return [0]

def get_entity_name(item, indices='all'):

    from sabueso.tools.sabueso_UniProtKB_XMLDict import get_entity_name as _get

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

