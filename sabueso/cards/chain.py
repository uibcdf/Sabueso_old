from .card import Card

class ChainCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.begin = None
        self.end = None
        self.index = None
        self.description = None

