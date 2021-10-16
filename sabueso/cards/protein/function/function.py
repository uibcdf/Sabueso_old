from sabueso.cards.card import Card
from copy import deepcopy
from pandas import DataFrame

class FunctionCard(Card):

    def __init__(self):

        super().__init__()

        self.protein_name = None
        self.protein_key_name = None
        self.protein_uniprot_id = None

        self.uniprot_function = None
        self.notes = []
        self.references = []

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

        return f'<ProteinFunctionCard: {self.protein_key_name}>'

