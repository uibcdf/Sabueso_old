
def get_function(item):

    from sabueso.cards.item.function import FunctionCard
    from sabueso.tools.uniprotkb_XMLDict import is_uniprotkb_XMLDict
    from sabueso.tools.uniprotkb_XMLDict import get_uniprotkb_XMLDict
    from sabueso.tools.uniprotkb_XMLDict import get_name as get_name_from_uniprotkb_XMLDict
    from sabueso.tools.uniprotkb_XMLDict import get_key_name as get_key_name_from_uniprotkb_XMLDict
    from sabueso.tools.uniprotkb_XMLDict import get_uniprot_id as get_uniprot_id_from_uniprotkb_XMLDict
    from sabueso.tools.uniprotkb_XMLDict import get_function as get_function_from_uniprotkb_XMLDict

    card = FunctionCard()

    if is_uniprotkb_XMLDict(item):
        uniprotkb_XMLDict = item
    else:
        uniprotkb_XMLDict = get_uniprotkb_XMLDict(item)

    card.protein_name = get_name_from_uniprotkb_XMLDict(uniprotkb_XMLDict)
    card.protein_key_name = get_key_name_from_uniprotkb_XMLDict(uniprotkb_XMLDict)
    card.protein_uniprot_id = get_uniprot_id_from_uniprotkb_XMLDict(uniprotkb_XMLDict)


    output_uniprotkb = get_function_from_uniprotkb_XMLDict(uniprotkb_XMLDict)

    card.uniprot_function = output_uniprotkb['function']
    card.notes += output_uniprotkb['notes']
    card.references += output_uniprotkb['references']

    return card

