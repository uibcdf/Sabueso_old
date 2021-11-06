from sabueso.forms import dict_convert
from sabueso._private_tools.lists_and_tuples import is_list_or_tuple
from sabueso._private_tools._digestion import *
from sabueso._private_tools.exceptions import *
from sabueso.get_form import get_form

def convert(item, to_form=None, indices='all'):

    if to_form is None:
        to_form = get_form(item)

    to_form = digest_to_form(to_form)

    if is_list_or_tuple(to_form):
        tmp_item=[]
        for aux_form in to_form:
            tmp_item.append(convert(item, to_form=aux_form, indices=indices))
        return tmp_item

    tmp_item = None

    item_form = get_form(item)

    tmp_item = dict_convert[item_form][to_form](item, indices=indices)

    tmp_item = digest_output(tmp_item)

    return tmp_item

