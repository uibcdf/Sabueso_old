class StackOfCards():

    def __init__(self):

        self.cards = {} # name: card

        self.n_ions = 0
        self.n_cosolutes = 0
        self.n_small_molecules = 0
        self.n_lipids = 0
        self.n_peptides = 0
        self.n_proteins = 0
        self.n_dnas = 0
        self.n_rnas = 0
        self.n_cards = 0

    def add(self, cards):

        pass

    def draw(self, name='all'):

        if name=='all':

            output = list(self.cards.values())

            self.n_ions = 0
            self.n_cosolutes = 0
            self.n_small_molecules = 0
            self.n_lipids = 0
            self.n_peptides = 0
            self.n_proteins = 0
            self.n_dnas = 0
            self.n_rnas = 0
            self.n_cards = 0

        else:

            raise NotImplementedError

        if len(output)==0:

            output = output[0]

        return output

