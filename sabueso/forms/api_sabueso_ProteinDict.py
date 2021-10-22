from evidence import Evidence

form_name='sabueso.ProteinDict'

is_form={
}

def to_string_uniprot_id(item, indices='all'):

    from .is_sabueso_ProteinDict import is_sabueso_ProteinDict
    from sabueso.tools.database_UniProtKB import query as query_UniProtKB

    output = None

    if not is_sabueso_ProteinDict(item):

        raise ValueError('The input argument is not a sabueso_ProteinDict item')

    query_string = f'''name:"{item['name']}" AND organism:"{item['organism']}"'''

    query_result = query_UniProtKB(query_string, output=['id', 'reviewed', 'protein names', 'organism', 'annotation score'])

    if query_result['Status'][0]!='reviewed':
        raise ValueError('The best result is not reviewed yet')

    if len(query_result)>1:

        if query_result['Annotation'][0]=='5 out of 5':
            if int(query_result['Annotation'][1][0])<5:
                output = query_result['Entry'][0]
            else:
                raise ValueError('The query string is not specific enough')
        else:
            raise ValueError('The query string is not specific enough')

    elif len(query_result)==1:

        if query_result['Annotation'][0]=='5 out of 5':
            output = query_result['Entry'][0]
        else:
            raise ValueError('The query string is not specific enough')

    else:
        pass

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

