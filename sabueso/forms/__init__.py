from importlib import import_module
import os

types = ['class', 'file', 'string']
forms = []

dict_type = {}
dict_is_form = {}
dict_get = {}

file_extensions_recognized = []
string_names_recognized = []

current_dir = os.path.dirname(os.path.abspath(__file__))

for dirname, typename in [['classes', 'class'], ['files', 'file'], ['strings', 'string']]:

    type_dir = os.path.join(current_dir, dirname)
    list_apis = [filename.split('.')[0] for filename in os.listdir(type_dir) if filename.startswith('api')]

    for api_name in list_apis:

        mod = import_module('sabueso.forms.'+dirname+'.'+api_name)

        form_name = mod.form_name
        forms.append(form_name)

        dict_type[form_name]=typename
        dict_is_form.update(mod.is_form)
        dict_get[form_name]= {'system':{}, 'entity':{}, }

        for method in mod.__dict__.keys():
            if method.startswith('get_'):
                option = method[4:]
                dict_get[form_name][option]=getattr(mod, method)



        del(mod, form_name)

    del(list_apis, type_dir)

for aux_form_name in list(dict_is_form.keys()):
    if type(aux_form_name) is str:
        if aux_form_name.startswith('file:'):
            file_extensions_recognized.append(aux_form_name.split(':')[-1].lower())
        elif aux_form_name.startswith('string:'):
            string_names_recognized.append(aux_form_name.split(':')[-1])

del(import_module, dirname, typename)


