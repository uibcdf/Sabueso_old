from importlib import import_module
import os

dict_get_cards = {}

current_dir = os.path.dirname(os.path.abspath(__file__))

list_apis = [filename.split('.')[0] for filename in os.listdir(current_dir) if filename.startswith('api')]

for api_name in list_apis:

    mod = import_module('sabueso.cards.forms.'+api_name)

    form_name = mod.form_name
    dict_get_cards[form_name] = mod.get_cards

    del(mod, form_name)

del(list_apis, import_module)


