from .card import Card

class SegmentCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.common_name = None
        self.scientific_name = None

