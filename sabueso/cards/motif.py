from .card import Card
from copy import deepcopy
from pandas import DataFrame

motif_dict = {
        'references':[],
        'description':None,
        'begin':None,
        'end':None,
        }

def is_motif_dict(item):

    output = False

    if type(item) is dict:
        if set(motif_dict)==set(item):
            output = True

    return output

class MotifCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'motif'

        if is_motif_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in motif_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(motif_dict)
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

        df = DataFrame(aux_dict, index =[self.begin+'-'+self.end])

        return df

    def __repr__(self):

        return f'<MotifCard: {self.description} {self.begin}-{self.end}>'

