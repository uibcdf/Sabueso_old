from .card import Card

class DomainCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.name = None
        self.begin = None
        self.end = None
        self.prosite_prorule = None

