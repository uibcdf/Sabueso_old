from .card import Card
from copy import deepcopy
from pandas import DataFrame


location_in_cell_dict = {
        'references':[],
        'location':[],
        'note':None,
        }

def is_location_in_cell_dict(item):

    output = False

    if type(item) is dict:
        if set(location_in_cell_dict)==set(item):
            output = True

    return output

class LocationInCellCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'location in cell'

        if is_location_in_cell_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in location_in_cell_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(location_in_cell_dict)
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

        df = DataFrame(aux_dict)

        return df

    def __repr__(self):

        return f'<LocationInCellCard: {self.location}>'

