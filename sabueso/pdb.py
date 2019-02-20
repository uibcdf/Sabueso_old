from .DBs.RCSB import card_pdb as _card_rcsb
from sabueso.fields.pdb import _pdb_dict

class PDB():

    def __init__(self, pdb=None, withverbose=True):

        self.type = 'PDB'
        self.pdb = pdb
        self.card = None

        if pdb is not None:
            tmp_card = _card_rcsb(pdb=pdb)
            self.card = tmp_card
            del(tmp_card,pdb)

    def make_Notebook(self):
        pass

    def dump(self,json_file=None):

        import json

        json_list = []
        json_list.append(json.dumps('PDB'))
        json_list.append(json.dumps(self.card))

        with open(json_file, 'w') as outfile:
            json.dump(json_list, outfile)

