from .entity import EntityCard

class PeptideCard(EntityCard):

    def __init__(self):

        super().__init__()

        self.uniprot = None

