from collections import OrderedDict
from evidence import Evidence

def get_alternative_names(item, entity='all'):

    from ._add_reference_to_evidence import _add_reference_to_evidence

    output = []

    accession = item['uniprot']['entry']['accession'][0]

    if 'shortName' in item['uniprot']['entry']['protein']['recommendedName']:
        evidence = Evidence()
        recommendedName = item['uniprot']['entry']['protein']['recommendedName']
        if type(recommendedName['shortName'])==str:
            evidence.value = recommendedName['shortName']
        else:
            evidence.value = recommendedName['shortName']['#text']
            if '@evidence' in recommendedName['shortName']:
                evidence_numbers_in_db = recommendedName['shortName']['@evidence'].split(' ')
                for evidence_number_in_db in evidence_numbers_in_db:
                    evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                    if evidence_in_db['@key']!=evidence_number_in_db:
                        raise ValueError('Evidence number does not match evidence @key')
                    _add_reference_to_evidence(evidence, evidence_in_db)
        evidence.add_reference({'database':'UniProtKB', 'id':accession})
        output.append(evidence)

    if 'alternativeName' in item['uniprot']['entry']['protein']:
        if type(['alternativeName'])==list:
            for alternativeName in item['uniprot']['entry']['protein']['alternativeName']:
                if 'fullName' in alternativeName:
                    evidence = Evidence()
                    if type(alternativeName['fullName'])==str:
                        evidence.value = alternativeName['fullName']
                    else:
                        evidence.value = alternativeName['fullName']['#text']
                        if '@evidence' in alternativeName['fullName']:
                            evidence_numbers_in_db = alternativeName['fullName']['@evidence'].split(' ')
                            for evidence_number_in_db in evidence_numbers_in_db:
                                evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                                if evidence_in_db['@key']!=evidence_number_in_db:
                                    raise ValueError('Evidence number does not match evidence @key')
                                _add_reference_to_evidence(evidence, evidence_in_db)
                    evidence.add_reference({'database':'UniProtKB', 'id':accession})
                    output.append(evidence)
                if 'shortName' in alternativeName:
                    evidence = Evidence()
                    if type(alternativeName['shortName'])==str:
                        evidence.value = alternativeName['shortName']
                    else:
                        evidence.value = alternativeName['shortName']['#text']
                        if '@evidence' in alternativeName['shortName']:
                            evidence_numbers_in_db = alternativeName['shortName']['@evidence'].split(' ')
                            for evidence_number_in_db in evidence_numbers_in_db:
                                evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                                if evidence_in_db['@key']!=evidence_number_in_db:
                                    raise ValueError('Evidence number does not match evidence @key')
                                _add_reference_to_evidence(evidence, evidence_in_db)
                    evidence.add_reference({'database':'UniProtKB', 'id':accession})
                    output.append(evidence)
        else:
            if 'fullName' in alternativeName:
                evidence = Evidence()
                if type(alternativeName['fullName'])==str:
                    evidence.value = alternativeName['fullName']
                else:
                    evidence.value = alternativeName['fullName']['#text']
                    if '@evidence' in alternativeName['fullName']:
                        evidence_numbers_in_db = alternativeName['fullName']['@evidence'].split(' ')
                        for evidence_number_in_db in evidence_numbers_in_db:
                            evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                            if evidence_in_db['@key']!=evidence_number_in_db:
                                raise ValueError('Evidence number does not match evidence @key')
                            _add_reference_to_evidence(evidence, evidence_in_db)
                evidence.add_reference({'database':'UniProtKB', 'id':accession})
                output.append(evidence)
            if 'shortName' in alternativeName:
                evidence = Evidence()
                if type(alternativeName['shortName'])==str:
                    evidence.value = alternativeName['shortName']
                else:
                    evidence.value = alternativeName['shortName']['#text']
                    if '@evidence' in alternativeName['shortName']:
                        evidence_numbers_in_db = alternativeName['shortName']['@evidence'].split(' ')
                        for evidence_number_in_db in evidence_numbers_in_db:
                            evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                            if evidence_in_db['@key']!=evidence_number_in_db:
                                raise ValueError('Evidence number does not match evidence @key')
                            _add_reference_to_evidence(evidence, evidence_in_db)
                evidence.add_reference({'database':'UniProtKB', 'id':accession})
                output.append(evidence)

    return output

