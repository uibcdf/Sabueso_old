from .entity import EntityCard


class ProteinCard(EntityCard):

    def __init__(self):

        super().__init__()

        self.references = []

        self.type = 'protein'                       # DB: UniProtKB, ChEMBL

        self.name = None                            # DB: UniProtKB, ChEMBL
        self.full_name = None                       # DB: UniProtKB
        self.short_name = None                      # DB: UniProtKB
        self.alternative_names = None               # DB: UniProtKB

        self.organism = None                        # DB: UniProtKB, ChEMBL

        self.host = None                            # DB: UniProtKB

        self.function = None                        # DB: UniProtKB

        self.subunit_structure = []                 # DB: UniProtKB

        self.sequence = None                        # DB: UniProtKB
        self.isoforms = []                          # DB: UniProtKB
        self.posttranslational_modifications = []   # DB: UniProtKB
        self.sequence_conflics = []                 # DB: UniProtKB
        self.alternative_sequences = []             # DB: UniProtKB

        self.secondary_structure = None             # DB: UniProtKB

        self.chains = None                          # DB: UniProtKB
        self.domains = None                         # DB: UniProtKB
        self.regions = None                         # DB: UniProtKB
        self.motifs = None                          # DB: UniProtKB

        self.binding_sites = None                   # DB: UniProtKB


        self.interactions = []                      # DB: UniProtKB
        self.ligands = []                           # DB: UniProtKB

        ### DBs

        self.uniprot = None                         # DB: UniProtKB
        self.ec = None                              # DB: UniProtKB
        self.chembl = None                          # DB: UniProtKB
        self.biogrid = None                         # DB: UniProtKB
        self.swiss_model = None                     # DB: UniProtKB
        self.dip = None                             # DB: UniProtKB
        self.elm = None                             # DB: UniProtKB
        self.intact = None                          # DB: UniProtKB
        self.mint = None                            # DB: UniProtKB
        self.bindingdb = None                       # DB: UniProtKB
        self.interpro = None                        # DB: UniProtKB
        self.pfam = None                            # DB: UniProtKB
        self.prodom = None                          # DB: UniProtKB
        self.supfam = None                          # DB: UniProtKB
        self.string = None                          # DB: UniProtKB
        self.iptmnet = None                         # DB: UniProtKB
        self.phosphositeplus = None                 # DB: UniProtKB

        ### PDBs

        self.pdbs = []                              # DB: UniProtKB
        self.segment_in_pdb = {}                    # DB: UniProtKB

        #self.pdbids100 = None
        #self.pdbids95 = None
        #self.pdbids75 = None

    def to_pandas_DataFrame(self):

        from pandas import DataFrame

        data = {
                'name':[self.name],
                'type':[self.type],
                'uniprot':[self.uniprot],
                'alternative names':[self.alternative_names],
                'organism common name':[self.organism_common_name],
                'organism scientific name':[self.organism_scientific_name],
                'host':[self.host],
                'canonical sequence':[self.canonical_sequence],
                'isoforms':[self.isoforms],
                'ec':[self.ec],
                'chembl':[self.chembl],
                'biogrid':[self.biogrid],
                'swiss_model':[self.swiss_model],
                'dip':[self.dip],
                'elm':[self.elm],
                'mint':[self.mint],
                'bindingdb':[self.bindingdb],
                'prodom':[self.prodom],
                'string':[self.string],
                'iptmnet':[self.iptmnet],
                'phosphositeplus':[self.phosphositeplus],
                'pdbs':[self.pdbs],
                }

        df = DataFrame(data, index =[self.name])

        return df

    def __repr__(self):

        df = self.to_pandas_DataFrame().T
        return repr(df)

