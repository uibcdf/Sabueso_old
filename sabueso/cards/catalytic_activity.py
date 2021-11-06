from .card import Card
from copy import deepcopy
from pandas import DataFrame

catalytic_activity_dict = {
        'references':[],
        'reaction':None,
        'physiological_direction':None,
        }

def is_catalytic_activity_dict(item):

    output = False

    if type(item) is dict:
        if set(catalytic_activity_dict)==set(item):
            output = True

    return output

class CatalyticActivityCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'catalytic_activity'

        if is_catalytic_activity_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in catalytic_activity_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(catalytic_activity_dict)
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

        df = DataFrame(aux_dict, index =[self.reaction.value])

        return df

    def __repr__(self):

        return f'<CatalyticActivityCard: {self.reaction.value}>'

