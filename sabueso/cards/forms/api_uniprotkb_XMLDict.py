
form_name = 'uniprotkb_XMLDict'

def get_cards(molecular_system, indices='all'):

    from sabueso.cards.entity_cards import ProteinCard
    from sabueso.cards.stack_of_cards import StackOfCards
    from sabueso.tools.uniprotkb_XMLDict import get_name
    from sabueso.tools.uniprotkb_XMLDict import get_alternative_names
    from sabueso.tools.uniprotkb_XMLDict import get_organism_common_name
    from sabueso.tools.uniprotkb_XMLDict import get_organism_scientific_name
    from sabueso.tools.uniprotkb_XMLDict import get_uniprot
    from sabueso.tools.uniprotkb_XMLDict import get_ec

    stack = StackOfCards()

    card = ProteinCard()

    card.name = get_name(molecular_system)
    card.alternative_names = get_alternative_names(molecular_system)

    card.organism_common_name = get_organism_common_name(molecular_system)
    card.organism_scientific_name = get_organism_scientific_name(molecular_system)

    card.uniprot = get_uniprot(molecular_system)
    card.ec = get_ec(molecular_system)

    stack.add(card)

    return stack

