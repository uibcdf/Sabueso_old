from .card import Card

class IsoformCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.begin = None
        self.end = None
        self.original = None
        self.modification = None
        self.sequence = None
        self.name = None
        self.uniprot = None

