from .card import Card
from copy import deepcopy
from pandas import DataFrame

secondary_structure_dict = {
        'references':[],
        'description':None,
        'helices':[],
        'strands':[],
        'turns':[],
        }

def is_secondary_structure_dict(item):

    output = False

    if type(item) is dict:
        if set(secondary_structure_dict)==set(item):
            output = True

    return output

class SecondaryStructureCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'secondary_structure'

        if is_secondary_structure_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in secondary_structure_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(secondary_structure_dict)
        for key in output:
            output[key]=getattr(self, key)

        return output

    def to_pandas_DataFrame(self, with_evidences=True):

        aux_dict = self.to_dict()
        for key in aux_dict:
            aux_dict[key]=[aux_dict[key]]

        if not with_evidences:
            for key in aux_dict:
                try:
                    aux_dict[key]=aux_dict[key][0].value
                except:
                    continue

        df = DataFrame(aux_dict, index =['ss'])

        return df

    def __repr__(self):

        return f'<SecondaryStructureCard: {len(self.helices)} helices, {len(self.strands)} strands and {len(self.turns)} turns>'

