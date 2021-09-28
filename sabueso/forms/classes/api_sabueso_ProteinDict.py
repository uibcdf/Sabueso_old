from evidence import Evidence

form_name='sabueso.ProteinDict'

is_form={
}

def this_dict_is_a_sabueso_ProteinDict(item):

    output = False

    if ('protein_name' in item) or ('uniprot_id' in item):
        output = True

    return output

###### Get

## General

def get_entity_index(item, indices='all'):

    return [0]

def get_entity_name(item, indices='all'):

    return [item['protein_name']]

def get_entity_id(item, indices='all'):

    return [None]

def get_entity_type(item, indices='all'):

    return ['protein']

def get_n_entities(item, indices='all'):

    return 1

## Protein

def get_organism(item, indices='all'):

    output = None

    if 'organism' in item:
        output = [item['organism']]
    elif 'uniprot_id' in item:
        from sabueso.forms.strings.api_uniprot_id import get_organism as get_organism_from_uniprot_id
        output = get_organis_from_uniprot_id(item['uniprot_id'])

    return output

def get_uniprot_id(item, indices='all'):

    entity_name = get_entity_name(item)
    organism = get_organism(item)


