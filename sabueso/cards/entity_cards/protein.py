from .entity import EntityCard

class ProteinCard(EntityCard):

    def __init__(self):

        super().__init__()


        self.type = 'protein'

        self.name = None # "The name corresponds to the recommended name by the UniProtKB"

        self.alternative_names = None

        self.organism_common_name = None
        self.organism_scientific_name = None

        self.uniprot = None
        self.ec = None

        self.sequence = None
        self.isoforms = None

        self.secondary_structure = None

        self.sites = None
        self.ligands = None

        self.pdbids100 = None
        self.pdbids95 = None

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
                }

        df = DataFrame(data, index =[self.name])

        return df

    def __repr__(self):

        df = self.to_pandas_DataFrame().T
        return repr(df)

