from sabueso.cards.entity import EntityCard
from copy import deepcopy
from pandas import DataFrame

protein_dict = {
        'references': [],
        'name': None,                               # DB: UniProtKB
        'key_name': None,                           # DB: UniProtKB
        'short_name': None,                         # DB: UniProtKB
        'uniprot_entry_name': None,                 # DB: UniProtKB
        'alternative_names': None,                  # DB: UniProtKB
        'family': None,                             # DB: UniProtKB
        'organism': None,                           # DB: UniProtKB
        'host': None,                               # DB: UniProtKB
        'location_in_cell': None,                   # DB: UniProtKB
        'tissue_specificity': None,                 # DB: UniProtKB
        'function': None,                           # DB: UniProtKB
        'catalytic_activity': None,                 # DB: UniProtKB
        'activity_regulation': None,                # DB: UniProtKB
        'metabolic_pathways': None,                 # DB: UniProtKB
        'subunit_structure': None,                  # DB: UniProtKB
        'sequence': None,                           # DB: UniProtKB
        'isoforms': [],                             # DB: UniProtKB
        'modified_residues': [],                    # DB: UniProtKB
        'natural_mutations': [],                    # DB: UniProtKB
        'artificial_mutations': [],                 # DB: UniProtKB
        'sequence_conflicts': [],                   # DB: UniProtKB
        #'posttranslational_modifications': [],     # DB: UniProtKB
        'secondary_structure': None,                # DB: UniProtKB
        'chains': [],                               # DB: UniProtKB
        'domains': [],                              # DB: UniProtKB
        'regions': [],                              # DB: UniProtKB
        'motifs': [],                               # DB: UniProtKB
        'nucleotide_binding_regions': [],           # DB: UniProtKB
        'dna_binding_regions': [],                  # DB: UniProtKB
        'zinc_finger_regions': [],                  # DB: UniProtKB
        'ca_binding_regions': [],                   # DB: UniProtKB
        'binding_sites': [],                        # DB: UniProtKB
        'diseases':[],                              # DB: UniProtKB
        'interactions':[],                          # DB: UniProtKB
        #'ligands': []                              # DB: UniProtKB
        'uniprot': None,                            # DB: UniProtKB
        'ec': None,                                 # DB: UniProtKB
        'chembl': None,                             # DB: UniProtKB
        'biogrid': None,                            # DB: UniProtKB
        'swiss_model': None,                        # DB: UniProtKB
        'dip': None,                                # DB: UniProtKB
        'elm': None,                                # DB: UniProtKB
        'intact': None,                             # DB: UniProtKB
        'mint': None,                               # DB: UniProtKB
        'bindingdb': None,                          # DB: UniProtKB
        'interpro': None,                           # DB: UniProtKB
        'pfam': None,                               # DB: UniProtKB
        'prodom': None,                             # DB: UniProtKB
        'supfam': None,                             # DB: UniProtKB
        'string': None,                             # DB: UniProtKB
        'iptmnet': None,                            # DB: UniProtKB
        'phosphositeplus': None,                    # DB: UniProtKB
        'other_comments': {},                    # DB: UniProtKB

        ### PDBs

        #self.pdbs = []                                 # DB: UniProtKB
        #self.segment_in_pdb = {}                       # DB: UniProtKB

        #self.pdbids100 = None
        #self.pdbids95 = None
        #self.pdbids75 = None

        }

def is_protein_dict(item):

    output = False

    if type(item) is dict:
        if set(organism_dict)==set(item):
            output = True

    return output


class ProteinCard(EntityCard):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'protein'

        if is_protein_dict(item):
            for key, value in item.items():
                setattr(self, key, value)
        else:
            for key, value in protein_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(protein_dict)
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
            aux_dict['alternative_names'][0]=[ii.value for ii in aux_dict['alternative_names'][0]]

        df = DataFrame(aux_dict, index =[self.name])

        return df

    def to_jupyter_notebook(self, filename=None):

        import nbformat as nbf
        from .notebooks import protein_notebook

        nb = protein_notebook(self)

        if filename is None:
            filename = f'{self.key_name.value}.ipynb'

        with open(filename, 'w') as fff:
            nbf.write(nb, fff)

        return filename

    def __repr__(self):

        return f'<ProteinCard: {self.name.value}, {self.organism.common_name.value}>'

