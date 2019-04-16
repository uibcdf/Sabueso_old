from copy import deepcopy as _deepcopy

def load(json_file=None):

    import json

    with open(json_file, "r") as read_file:
        sabueso_json = json.load(read_file)

    if sabueso_json[0] == '"Protein"':
        from .protein import Protein as _Protein
        tmp_item = _Protein()
        tmp_item.card = json.loads(sabueso_json[1])
        del(_Protein)

    del(sabueso_json)
    return tmp_item

def pretty_print(cards=None, summary=True):

    import pandas as pd

    is_list=False
    if type(cards) in [list,tuple]:
        is_list=True

    is_type=None
    if is_list:
        is_type=cards[0]['Type'][0]
    else:
        is_type=cards['Type'][0]


    if is_type in ['Protein', 'SINGLE PROTEIN']:
        is_type='Protein'

    tmp_df = pd.DataFrame(cards)
    if summary:
        if is_type=='Protein':
            tmp_df=tmp_df[['Name', 'Full Name', 'Short Name', 'Alternative Name', 'Host',
                           'UniProt', 'ChEMBL','Type']]

    return tmp_df

