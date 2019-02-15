from .DBs.UniProt import initialize_protein as _initialize_uniprot
from .DBs.ChEMBL import data_to_protein as _data_chembl

_protein_keys   = ['Name',                # Db: UniProt, ChEMBL
                   'Full Name',           # Db: UniProt
                   'Short Name',          # Db: UniProt
                   'Alternative Name',    # Db: UniProt
                   'Type',                # Db: ChEMBL
                   'Organism',            # Db: UniProt, ChEMBL
                   'Host',                # Db: UniProt
                   'Function',            # Db: UniProt
                   'UniProt',             # Db: UniProt, ChEMBL
                   'Sequence',            # Db: UniProt
                   'FASTA',               # Db: UniProt
                   'ChEMBL',              # Db: UniProt, ChEMBL
                   'BioGRID',             # Db: UniProt
                   'ProteinModelPortal',  # Db: UniProt
                   'Swiss-Model',         # Db: UniProt
                   'DIP',                 # Db: UniProt
                   'ELM',                 # Db: UniProt
                   'IntAct',              # Db: UniProt, ChEMBL
                   'MINT',                # Db: UniProt
                   'BindingDB',           # Db: UniProt,
                   'InterPro',            # Db: UniProt, ChEMBL
                   'Pfam',                # Db: UniProt, ChEMBL
                   'ProDom',              # Db: UniProt
                   'PDB',                 # Db: UniProt, ChEMBL
                   'SUPFAM',              # Db: UniProt
                   'Mutagenesis']


class Protein():

    def __init__(self,UniProt=None,verbose=True):

        self.type = 'Protein'
        self.card = {key:[] for key in _protein_keys}
        self._uniprot=UniProt

        _initialize_uniprot(self)
        _data_chembl(self)

    def make_Notebook(self):
        pass

    def dump(self):
        pass

    def load(self):
        pass
