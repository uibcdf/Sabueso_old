import evidence as evi
from copy import deepcopy

def get_binding_sites(item, entity='all', as_cards=False):

    from sabueso.cards import BindingSiteCard, binding_site_dict
    from ._add_reference_to_evidence import _add_reference_to_evidence
    from ._get_reference_from_dbevidence import _get_reference_from_dbevidence
    from .get_uniprot import get_uniprot

    output = []

    uniprot = get_uniprot(item, entity=entity)
    ref_uniprot = uniprot.references[0]

    for feature in item['uniprot']['entry']['feature']:

        if feature['@type']=='binding site':
            aux_dict=deepcopy(binding_site_dict)
            aux_dict['description']=feature['@description']
            aux_dict['position']=feature['location']['position']['@position']
            aux_dict['references'].append(ref_uniprot)
            if '@evidence' in feature:
                evidence_numbers = feature['@evidence'].split(' ')
                for ii in evidence_numbers:
                    ref = _get_reference_from_dbevidence(int(ii), item)
                    if ref is not None:
                        aux_dict['references'].append(ref)
            output.append(aux_dict)

    if as_cards:
        output = [BindingSiteCard(ii) for ii in output]

    return output

