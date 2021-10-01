from importlib import import_module
import os

types = ['class', 'file', 'string']
forms = []

dict_type = {}
dict_is_form = {}
dict_is_ion = {}
dict_is_water = {}
dict_is_cosolute = {}
dict_is_small_molecule = {}
dict_is_lipid = {}
dict_is_peptide = {}
dict_is_protein = {}
dict_is_rna = {}
dict_is_dna = {}
dict_get = {}

file_extensions_recognized = []
string_names_recognized = []

current_dir = os.path.dirname(os.path.abspath(__file__))

list_apis = [filename.split('.')[0] for filename in os.listdir(current_dir) if filename.startswith('api_')]

for api_name in list_apis:

    mod = import_module('sabueso.forms.'+api_name)

    form_name = mod.form_name
    forms.append(form_name)

    if form_name.startswith('string:'):
        form_type = 'string'
    elif form_name.startswith('file:'):
        form_type = 'file'
    else:
        form_type = 'class'

    dict_type[form_name] = form_type
    dict_is_form.update(mod.is_form)
    dict_is_ion[form_name] = mod.is_ion
    dict_is_water[form_name] = mod.is_water
    dict_is_cosolute[form_name] = mod.is_cosolute
    dict_is_small_molecule[form_name] = mod.is_small_molecule
    dict_is_peptide[form_name] = mod.is_peptide
    dict_is_protein[form_name] = mod.is_protein
    dict_is_rna[form_name] = mod.is_rna
    dict_is_dna[form_name] = mod.is_dna
    dict_get[form_name] = {}

    for method in mod.__dict__.keys():
        if method.startswith('get_'):
            option = method[4:]
            dict_get[form_name][option]=getattr(mod, method)



    del(mod, form_name, form_type)

del(list_apis, import_module)

for aux_form_name in list(dict_is_form.keys()):
    if type(aux_form_name) is str:
        if aux_form_name.startswith('file:'):
            file_extensions_recognized.append(aux_form_name.split(':')[-1].lower())
        elif aux_form_name.startswith('string:'):
            string_names_recognized.append(aux_form_name.split(':')[-1])


