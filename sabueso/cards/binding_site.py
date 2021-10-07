from .card import Card

class BindingSiteCard(Card):

    def __init__(self):

        super().__init__()

        self.references = []

        self.residues = None

