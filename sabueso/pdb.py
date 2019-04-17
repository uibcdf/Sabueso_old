from .DBs.RCSB import pdb_card as _pdb_card_rcsb
from .DBs.PDBe import pdb_card as _pdb_card_pdbe

class PDB():

    def __init__(self, pdb=None, withverbose=True):

        self.type = 'PDB'
        self.pdb = pdb
        self.card = None

        if pdb is not None:
            tmp_card = _pdb_card_rcsb(pdb=pdb)
            tmp_card = _pdb_card_pdbe(pdb=pdb,card=tmp_card)
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

    def info(self):

        from .utils import get_sequence as _get_sequence

        print("\n")
        print(">>> {}: {}".format(self.card["Id"],self.card["Title"]))
        print("\n")
        print("List of Entities:")
        print("\n")
        for entitity_id, entity_card in self.card["Entity"].items():
            if entity_card['Type'] in ["polymer"]:
                if entity_card['Description'].startswith('DNA'):
                    print("\t{}".format(entity_card['Description']))
                    print("\tType: {}".format(entity_card['Type']))
                    print("\tChains: {}".format(entity_card['Chains']))
                else:
                    print("\t{} (UniProt:{})".format(entity_card['Description'],entity_card['UniProt']))
                    print("\tType: {}".format(entity_card['Type']))
                    print("\tChains: {}".format(entity_card['Chains']))
                    len_solved = len(entity_card['Sequence'])
                    if entity_card['UniProt'] is not None:
                        len_polymer = len(_get_sequence(entity_card['UniProt']))
                    else:
                        len_polymer = 'Unknown'
                    print("\tLength of polymer: {} of {} aminoacids".format(len_solved,len_polymer))
            else:
                print("\t{}".format(entity_card['Description']))
                print("\tType: {}".format(entity_card['Type']))
                print("\tChains: {}".format(entity_card['Chains']))
            print("\n")
        print("Method and Resolution: {}, {}".format(self.card["Method"][0], self.card["Resolution"]))
        if self.card["Number Models"]>1:
            print("Number of Models: {}".format(self.card["Number Models"]))
        print("\n")
