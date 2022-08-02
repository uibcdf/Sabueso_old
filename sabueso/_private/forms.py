from sabueso.forms import forms
from sabueso._private.lists_and_tuples import is_list_or_tuple
from sabueso._private.exceptions import *

form_from_lowercase = {ii.lower():ii for ii in forms}

def digest_form(form):

    if form_is_file(form):
        output = form
    elif is_list_or_tuple(form):
        output = [digest_form(ii) for ii in form]
    else:
        try:
            output = form_from_lowercase[form.lower()]
        except:
            raise NotImplementedFormError()

    return output

def digest_to_form(to_form):

    if to_form is None:
        return None
    else:
        return digest_form(to_form)

def to_form_is_file(to_form):

    return form_is_file(to_form)

def form_is_file(form):

    output = False

    if type(form) is str:
        if ':' not in form:
            if item_is_file(form):
                output = True

    return output

def form_of_file(to_form):

    output = None

    if form_is_file(to_form):
        output = item_is_file(to_form)

    return output

def item_is_file(item):

    from sabueso.forms import file_extensions_recognized

    output = False

    if type(item) is str:
        file_extension = item.split('.')[-1].lower()
        if file_extension in file_extensions_recognized:
            output = 'file:'+file_extension

    return output

#def item_is_string(item):
#
#    from sabueso.forms import string_names_recognized
#    from .strings import guess_form_from_string
#
#    output = False
#
#    if type(item) is str:
#        if ':' in item:
#            string_name = item.split(':')[0]
#            if string_name in string_names_recognized:
#                output = 'string:'+string_name
#        if output==False:
#            output = guess_form_from_string(item)
#            if output is None:
#                output = False
#
#    return output

