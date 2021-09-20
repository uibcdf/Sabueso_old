from importlib import import_module
import os
from molsysmt.forms.loader import api_to_be_loaded, converts_to_be_loaded, modules_detected

types = ['class', 'file', 'string']
forms = []

dict_type = {}
dict_is_form = {}

file_extensions_recognized = []
string_names_recognized = []


current_dir = os.path.dirname(os.path.abspath(__file__))

for dirname, typename in [['classes', 'class'], ['files', 'file'], ['strings', 'string']]:

    type_dir = os.path.join(current_dir, dirname)
    list_apis = [filename.split('.')[0] for filename in os.listdir(type_dir) if filename.startswith('api')]

    for api_name in list_apis:

        if api_to_be_loaded[api_name]:

            mod = import_module('molsysmt.forms.'+dirname+'.'+api_name)

            form_name = mod.form_name
            forms.append(form_name)

            dict_type[form_name]=typename
            dict_is_form.update(mod.is_form)

for aux_form_name in list(dict_is_form.keys()):
    if type(aux_form_name) is str:
        if aux_form_name.startswith('file:'):
            file_extensions_recognized.append(aux_form_name.split(':')[-1].lower())
        elif aux_form_name.startswith('string:'):
            string_names_recognized.append(aux_form_name.split(':')[-1])

