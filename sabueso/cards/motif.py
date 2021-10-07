from .card import Card

class MotifCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.begin = None
        self.end = None
        self.note = None

