
def to_string_uniprot(item, entity='all'):

    from .get_uniprot import get_uniprot

    uniprot = get_uniprot(item, entity=entity)

    output = 'uniprot:'+uniprot.value

    return output
