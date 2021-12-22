from evidence import Evidence

form_name='sabueso.ProteinDict'

is_form={
}

from sabueso.tools.sabueso_ProteinDict.to_string_uniprot_id import to_string_uniprot_id

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

## Is entity

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

## Protein

#def get_organism(item, indices='all'):

    #output = None

    #if 'organism' in item:
    #    output = [item['organism']]
    #elif 'uniprot_id' in item:
    #    from sabueso.forms.strings.api_uniprot_id import get_organism as get_organism_from_uniprot_id
    #    output = get_organis_from_uniprot_id(item['uniprot_id'])

    #return output

#def get_uniprot_id(item, indices='all'):

    #entity_name = get_entity_name(item)
    #organism = get_organism(item)

#    raise NotImplementedError

