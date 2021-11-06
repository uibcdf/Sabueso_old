from .card import Card

class PostTranslationalModificationCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.modified_residues = None
        self.cross_link = None


