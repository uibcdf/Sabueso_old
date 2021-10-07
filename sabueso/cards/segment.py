from .card import Card

class SegmentCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.begin = None
        self.end = None
        self.length = None
        self.chain = None
        self.entity = None

