from collections import OrderedDict
from evidence import Evidence

def get_ec(item, entity='all'):

    from ._add_reference_to_evidence import _add_reference_to_evidence

    if 'ecNumber' in item['uniprot']['entry']['protein']['recommendedName']:

        ecNumber = item['uniprot']['entry']['protein']['recommendedName']['ecNumber']
        evidence = Evidence()

        if '#text' in ecNumber:
            evidence.value = ecNumber['#text']
        if '@evidence' in ecNumber:
            evidence_numbers_in_db = ecNumber['@evidence'].split()
            for evidence_number_in_db in evidence_numbers_in_db:
                evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                if evidence_in_db['@key']!=evidence_number_in_db:
                    raise ValueError('Evidence number does not match evidence @key')
                _add_reference_to_evidence(evidence, evidence_in_db)

    accession = item['uniprot']['entry']['accession'][0]
    evidence.add_UniProtKB(id=accession)

    return evidence

