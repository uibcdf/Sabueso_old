from .entity import EntityCard

class ProteinCard(EntityCard):

    def __init__(self):

        super().__init__()

        self.uniprot = None

