from .card import Card
from copy import deepcopy
from pandas import DataFrame

interactant_dict = {
        'references':[],
        'type':None,
        'name':None,
        'intact':None,
        'uniprot':None,
        'mutations':None,
        'isoform_specific':None,
        }

def is_interactant_dict(item):

    output = False

    if type(item) is dict:
        if set(interactant_dict)==set(item):
            output = True

    return output


class InteractantCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'interactant'

        if is_interactant_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in interactant_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(interactant_dict)
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

        df = DataFrame(aux_dict, index =[self.name])

        return df

    def __repr__(self):

        if self.name is not None:
            return f'<InteractantCard: {self.type}, {self.name}>'
        elif self.intact is not None:
            return f'<InteractantCard: {self.type}, {self.intact}>'
        else:
            return f'<InteractantCard: unknown>'

