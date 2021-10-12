import evidence as evi
from copy import deepcopy

def get_regions(item, entity='all', as_cards=False):

    from sabueso.cards import RegionCard, region_dict
    from ._add_reference_to_evidence import _add_reference_to_evidence
    from ._get_reference_from_dbevidence import _get_reference_from_dbevidence

    output = []

    accession = item['uniprot']['entry']['accession'][0]
    ref_uniprot = evi.reference({'database':'UniProtKB', 'id':accession})

    for feature in item['uniprot']['entry']['feature']:

        if feature['@type']=='region of interest':
            aux_dict=deepcopy(region_dict)
            aux_dict['description']=feature['@description']
            aux_dict['begin']=feature['location']['begin']['@position']
            aux_dict['end']=feature['location']['end']['@position']
            aux_dict['references'].append(ref_uniprot)
            if '@evidence' in feature:
                evidence_numbers = feature['@evidence'].split(' ')
                for ii in evidence_numbers:
                    ref = _get_reference_from_dbevidence(int(ii), item)
                    if ref is not None:
                        aux_dict['references'].append(ref)
            output.append(aux_dict)

    if as_cards:
        output = [RegionCard(ii) for ii in output]

    return output

