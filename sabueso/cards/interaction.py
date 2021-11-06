from .card import Card
from copy import deepcopy
from pandas import DataFrame

interaction_dict = {
        'references':[],
        'interactants':[],
        'n_experiments':None,
        'same_organism':None,
        'intact':None,
        'imex':None,
        'with_mutations':None,
        }

def is_interaction_dict(item):

    output = False

    if type(item) is dict:
        if set(interaction_dict)==set(item):
            output = True

    return output


class InteractionCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'interaction'

        if is_interaction_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in interaction_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(interaction_dict)
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

        df = DataFrame(aux_dict, index =[self.ebi])

        return df

    def __repr__(self):

        return f'<InteractionCard: {self.interactants}>'

