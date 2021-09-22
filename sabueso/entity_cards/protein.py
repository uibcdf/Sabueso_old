from .entity import EntityCard

class ProteinCard(EntityCard):

    def __init__(self):

        super().__init__()


        self.type = 'protein'

        self.name = None # "The name corresponds to the recommended name by the UniProtKB"

        self.alternative_names = None

        self.organism = None

        self.uniprot = None
        self.ec = None

        self.sequence = None
        self.isoforms = None

        self.secondary_structure = None

        self.sites = None
        self.ligands = None

        self.pdbids100 = None
        self.pdbids95 = None

