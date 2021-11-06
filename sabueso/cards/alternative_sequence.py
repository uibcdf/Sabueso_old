from .card import Card

class AlternativeSequenceCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.begin = None
        self.end = None
        self.description = None

