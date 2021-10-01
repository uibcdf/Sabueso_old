
form_name = 'uniprotkb_XMLDict'

def get_cards(molecular_system, indices='all'):

    from sabueso.cards.entity_cards import ProteinCard
    from sabueso.cards.stack_of_cards import StackOfCards
    from sabueso.forms.api_uniprotkb_XMLDict import _add_reference_to_evidence, get_entity_name

    stack = StackOfCards()

    card = ProteinCard()

    card.name = get_entity_name(molecular_system)

    card.alternative_names = None

    card.organism = None

    card.uniprot = None

    stack.add(card)

    return stack

