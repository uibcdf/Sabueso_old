from sabueso.forms import forms
from sabueso._private.lists_and_tuples import is_list_or_tuple
from sabueso._private.exceptions import *

form_from_lowercase = {ii.lower():ii for ii in forms}

def item_is_file(item):

    from sabueso.forms import file_extensions_recognized

    output = False

    if type(item) is str:
        file_extension = item.split('.')[-1].lower()
        if file_extension in file_extensions_recognized:
            output = 'file:'+file_extension

    return output

def item_is_string(item):

    from sabueso.forms import string_names_recognized
    from .strings import guess_form_from_string

    output = False

    if type(item) is str:
        if ':' in item:
            string_name = item.split(':')[0]
            if string_name in string_names_recognized:
                output = 'string:'+string_name
        if output==False:
            output = guess_form_from_string(item)
            if output is None:
                output = False

    return output

