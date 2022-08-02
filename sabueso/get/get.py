from sabueso.get_form import get_form
from sabueso.forms import dict_get
from .arguments import digest_argument
from sabueso._private._digestion import *

def get(molecular_system, selection='all', syntaxis='sabueso', **kwargs):

    form = get_form(molecular_system)
    if type(molecular_system) is str:
        molecular_system = digest_string(molecular_system, form)

    attributes = [ digest_argument(key) for key in kwargs.keys() if kwargs[key] ]

    if selection is not 'all':
        raise NotImplementedError('Selection different from "all" not implemented')
    else:
        indices = 'all'

    output = []

    for attribute in attributes:

        result = dict_get[form][attribute](molecular_system, indices=indices)

        output.append(result)

    output=digest_output(output)

    return output

