import evidence as evi
from collections import OrderedDict

def get_function(item, entity='all'):

    from ._add_reference_to_evidence import _add_reference_to_evidence
    from .get_uniprot import get_uniprot

    output = []

    uniprot = get_uniprot(item, entity=entity)
    ref_uniprot = uniprot.references[0]

    ### Info in comment

    for comment in item['uniprot']['entry']['comment']:

        if comment['@type']=='function':

            if type(comment)!=OrderedDict:
                raise ValueError("Comment type not recognized for function")

            comment_text = comment['text']

            if type(comment_text)==OrderedDict:
                comment_text = list(comment_text)
            elif type(comment_text)==str:
                comment_text = [comment_text]

            if type(comment_text)!=list:
                raise ValueError("Text in comment not recognized for function")

            for aux in comment_text:

                evidence = evi.Evidence()

                if type(aux)==OrderedDict:

                    evidence.value = aux['#text']

                    if '@evidence' in aux:
                        evidence_numbers_in_db = aux['@evidence'].split(' ')
                        for evidence_number_in_db in evidence_numbers_in_db:
                            evidence_in_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
                            if evidence_in_db['@key']!=evidence_number_in_db:
                                raise ValueError('Evidence number does not match evidence @key')
                            _add_reference_to_evidence(evidence, evidence_in_db)

                elif type(aux)==str:
                    evidence.value = aux

                evidence.add_reference(ref_uniprot)

                output.append(evidence)

    return output

