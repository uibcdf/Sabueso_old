from .entity import EntityCard

class ProteinCard(EntityCard):

    def __init__(self):

        super().__init__()


        self.type = 'protein'

        self.name = None # "The name corresponds to the recommended name by the UniProtKB"

        self.alternative_names = None

        self.organism_common_name = None
        self.organism_scientific_name = None

        self.host = None

        #self.sequence = None
        #self.isoforms = None

        #self.secondary_structure = None

        #self.sites = None
        #self.ligands = None

        #self.pdbids100 = None
        #self.pdbids95 = None

        ### DBs

        self.uniprot = None
        self.ec = None
        self.chembl = None
        self.biogrid = None
        self.proteinmodelportal = None
        self.swiss_model = None
        self.dip = None
        self.elm = None
        self.intact = None
        self.mint = None
        self.bindingdb = None
        self.prodom = None
        self.string = None
        self.iptmnet = None
        self.phosphositeplus = None

        ### PDBs

        self.pdbs = None

    def to_pandas_DataFrame(self):

        from pandas import DataFrame

        data = {
                'name':[self.name],
                'type':[self.type],
                'alternative names':[self.alternative_names],
                'organism common name':[self.organism_common_name],
                'organism scientific name':[self.organism_scientific_name],
                'uniprot':[self.uniprot],
                'ec':[self.ec],
                'chembl':[self.chembl],
                'biogrid':[self.biogrid],
                'proteinmodelportal':[self.proteinmodelportal],
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

