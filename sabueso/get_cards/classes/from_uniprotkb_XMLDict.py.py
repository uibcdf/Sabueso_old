

def from_uniprotkb_XMLDict(molecular_system, indices='all'):

    from sabueso.entity_cards import ProteinCard
    from sabueso.forms.classes.api_uniprotkb_XMLDict import _add_reference_to_evidence
    from sabueso.forms.classes.api_uniprotkb_XMLDict import get_entity_name

    card = ProteinCard()

    card.name = get_entity_name(molecular_system)

    card.alternative_names = None

    card.organism = None

    card.uniprot = None



