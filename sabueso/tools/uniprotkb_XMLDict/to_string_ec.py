
def to_string_ec(item, entity='all'):

    from .get_ec import get_ec

    ec = get_ec(item, entity=entity)

    output = 'ec:'+ec.value

    return output
