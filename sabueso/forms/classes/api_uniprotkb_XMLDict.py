from evidence import Evidence
from collections import OrderedDict

form_name='uniprotkb.XMLDict'

is_form={
}

def this_dict_is_a_uniprotkb_XMLDict(item):

    return list(item.keys())==['uniprot']

###### Get

def _add_reference_to_evidence(evidence, evidence_in_db):

    if 'source' in evidence_in_db:
        if 'dbReference' in evidence_in_db['source']:

            dbtype = evidence_in_db['source']['dbReference']['@type']
            dbid = evidence_in_db['source']['dbReference']['@id']

            if dbtype=='UniProtKB':
                evidence.add_UniProtKB(id=dbid)
            elif dbtype=='PubMed':
                evidence.add_PubMed(id=dbid)
            elif dbtype=='DOI':
                evidence.add_PubMed(id=dbid)
            else:
                raise ValueError('Uknown source')

def get_entity_index(item, indices='all'):

    return [0]

def get_entity_name(item, indices='all'):

    output = []

    entity_name = Evidence()

    fullName = item['uniprot']['entry']['protein']['recommendedName']['fullName']

    if type(fullName)==str:
        entity_name.value=fullName
    elif type(fullName)==OrderedDict:
        if '#text' in fullName:
            entity_name.value = fullName['#text']
        if '@evidence' in fullName:
            evidence_number_in_db = fullName['@evidence']
            evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
            if evidence_in_db['@key']!=evidence_number_in_db:
                raise ValueError('Evidence number does not match evidence @key')
            _add_reference_to_evidence(entity_name, evidence_in_db)

    accession = item['uniprot']['entry']['accession'][0]
    entity_name.add_UniProtKB(id=accession)

    output.append(entity_name)

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

