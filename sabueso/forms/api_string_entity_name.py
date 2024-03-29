form_name='string:entity_name'

is_form = {
        'string:entity_name': form_name
    }

from sabueso.tools.string_entity_name.to_string_uniprot_id import to_string_uniprot_id

###### Get

def get_entity_index(item, indices='all'):

    return [0]

def get_entity_name(item, indices='all'):

    raise NotImplementedError()

def get_entity_id(item, indices='all'):

    return [None]

def get_entity_type(item, indices='all'):

    raise NotImplementedError()

def get_n_entities(item, indices='all'):

    return 1

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

    from sabueso.forms.strings.api_string_entity_name import to_string_uniprot_id

    output = False

    try:
        uniprot_id = to_string_uniprot_id(item, max_results=200)
        if uniprot_id:
            output = True
    except:
        pass

    return [output]

def is_rna(item, indices='all'):

    raise NotImplementedError()

def is_dna(item, indices='all'):

    raise NotImplementedError()

