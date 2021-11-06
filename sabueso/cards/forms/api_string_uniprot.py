form_name = 'string:uniprot'

def get_cards(molecular_system, indices='all'):

    from sabueso.tools.string_uniprot import to_uniprotkb_XMLDict
    from sabueso.cards.forms.api_uniprotkb_XMLDict import get_cards as get_cards_from_uniprotkb_XMLDict

    tmp_molecular_system = to_uniprotkb_XMLDict(molecular_system)
    stack = get_cards_from_uniprotkb_XMLDict(tmp_molecular_system, indices=indices)

    return stack

