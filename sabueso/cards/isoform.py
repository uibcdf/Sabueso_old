from .card import Card
from copy import deepcopy
from pandas import DataFrame

isoform_dict = {
        'references':[],
        'name':None,
        'alternative_names':None,
        'type':None,
        'sequence':None,
        'begin':None,
        'end':None,
        'original':None,
        'variation':None,
        'vsp':None,
        'uniprot':None,
        }


def is_isoform_dict(item):

    output = False

    if type(item) is dict:
        if set(isoform_dict)==set(item):
            output = True

    return output


class IsoformCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'isoform'

        if is_isoform_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in isoform_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(isoform_dict)
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

        return f'<IsoformCard: {self.name}>'

