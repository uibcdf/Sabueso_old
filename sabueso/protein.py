from .DBs.UniProt import card_protein as _card_uniprot
from .DBs.ChEMBL import card_protein as _card_chembl

def _remove_duplicates_from_card(card):

    for key in card.keys():
        if key not in ['Interactions','Sequence','Structure','Experimental Evidences',
                      'PBD']:
            card[key] = list(set(card[key]))


class Protein():

    def __init__(self, uniprot=None, withverbose=True):

        self.type = 'Protein'
        self.card = None

        tmp_card = _card_uniprot(uniprot=uniprot)
        tmp_card = _card_chembl(card=tmp_card)
        #_remove_duplicates_from_card(tmp_card)
        self.card = tmp_card
        del(tmp_card,uniprot)

    def make_Notebook(self):
        pass

    def dump(self):
        pass

    def load(self):
        pass
