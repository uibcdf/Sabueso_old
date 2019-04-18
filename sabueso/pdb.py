from molmodel import PDB as _mme_PDB
from .DBs.RCSB import dress_pdb as _rcsb_dress_pdb
from .DBs.PDBe import dress_pdb as _pdbe_dress_pdb

### The PDB class is fulfilled with the following sequence:
#
#   1.- RCSB:
#           - Basic info from MMTF file
#   2.- PDBe
#   3.- ...

class PDB(_mme_PDB):

    def __init__(self, pdb_id=None, load=True):

        super(_mme_PDB,self).__init__(pdb_id=pdb_id)

        if load:
            _rcsb_dress_pdb(self)
            #_pdbe_dress_pdb(self)

    def make_Notebook(self):
        pass

    #def dump(self,json_file=None):

    #    import json

    #    json_list = []
    #    json_list.append(json.dumps('PDB'))
    #    json_list.append(json.dumps(self.card))

    #    with open(json_file, 'w') as outfile:
    #        json.dump(json_list, outfile)

    #def info(self):

    #    from .utils import get_sequence as _get_sequence

    #    print("\n")
    #    print(">>> {}: {}".format(self.card["Id"],self.card["Title"]))
    #    print("\n")
    #    print("List of Entities:")
    #    print("\n")
    #    for entitity_id, entity_card in self.card["Entity"].items():
    #        if entity_card['Type'] in ["polymer"]:
    #            if entity_card['Description'].startswith('DNA'):
    #                print("\t{}".format(entity_card['Description']))
    #                print("\tType: {}".format(entity_card['Type']))
    #                print("\tChains: {}".format(entity_card['Chains']))
    #            else:
    #                print("\t{} (UniProt:{})".format(entity_card['Description'],entity_card['UniProt']))
    #                print("\tType: {}".format(entity_card['Type']))
    #                print("\tChains: {}".format(entity_card['Chains']))
    #                len_solved = len(entity_card['Sequence'])
    #                if entity_card['UniProt'] is not None:
    #                    len_polymer = len(_get_sequence(entity_card['UniProt']))
    #                else:
    #                    len_polymer = 'Unknown'
    #                print("\tLength of polymer: {} of {} aminoacids".format(len_solved,len_polymer))
    #        else:
    #            print("\t{}".format(entity_card['Description']))
    #            print("\tType: {}".format(entity_card['Type']))
    #            print("\tChains: {}".format(entity_card['Chains']))
    #        print("\n")
    #    print("Method and Resolution: {}, {}".format(self.card["Method"][0], self.card["Resolution"]))
    #    if self.card["Number Models"]>1:
    #        print("Number of Models: {}".format(self.card["Number Models"]))
    #    print("\n")

