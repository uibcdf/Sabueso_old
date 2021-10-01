from collections import OrderedDict
from evidence import Evidence

def get_entity_name(item, entity='all'):

    from ._add_reference_to_evidence import _add_reference_to_evidence

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

    return entity_name

