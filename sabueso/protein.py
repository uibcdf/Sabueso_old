from .DBs.UniProt import protein_card as _protein_card_uniprot
from .DBs.ChEMBL import protein_card as _protein_card_chembl

def _remove_duplicates_from_card(card):

    for key in card.keys():
        if key not in ['Interactions','Sequence','Structure','Experimental Evidences',
                      'PBD']:
            if type(card[key])==list:
                print(key)
                card[key] = list(set(card[key]))


class Protein():

    def __init__(self, uniprot_id=None, with_pdbs=True):

        self.type = 'Protein'
        self.card = None

        if uniprot_id is not None:
            tmp_card = _protein_card_uniprot(uniprot_id=uniprot_id)
            if len(tmp_card['ChEMBL'])>0:
                tmp_card = _protein_card_chembl(card=tmp_card)
            #_remove_duplicates_from_card(tmp_card)
            self._build_pdbs()
            self.card = tmp_card
            del(tmp_card,uniprot_id)

    def make_Notebook(self):
        pass

    def dump(self,json_file=None):

        import json

        json_list = []
        json_list.append(json.dumps('Protein'))
        json_list.append(json.dumps(self.card))

        with open(json_file, 'w') as outfile:
            json.dump(json_list, outfile)

    def drop_pdb(self,pdb_id=None):
        pass

    def add_pdb(self,pdb_id=None):
        pass

    def _build_pdbs():
        pass

