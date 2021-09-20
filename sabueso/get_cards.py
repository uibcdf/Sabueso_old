def get_cards(molecular_system, molecule_index='all'):

    form = get_form(molecular_system)

    output = dict_get_cards[form](molecular_system)

    if stack.n_cards == 1:

        output = stack.draw()[0]

    return output

