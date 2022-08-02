class StackOfCards():

    def __init__(self):

        self.card = {} # name: card

        self.n_ions = 0
        self.n_waters = 0
        self.n_cosolutes = 0
        self.n_small_molecules = 0
        self.n_lipids = 0
        self.n_peptides = 0
        self.n_proteins = 0
        self.n_dnas = 0
        self.n_rnas = 0
        self.n_cards = 0

    def __repr__(self):

        text= f'<StackOfCards with {self.n_cards} cards'

        if self.n_cards:
            text +='>'
        else:
            text +='>'

        return text

    def add(self, cards):

        from sabueso._private.lists_and_tuples import is_list_or_tuple

        if not is_list_or_tuple(cards):
            cards=[cards]

        for card in cards:
            self.card[card.name.value]=card
            if card.type == 'ion':
                self.n_ions+=1
            elif card.type == 'water':
                self.n_waters+=1
            elif card.type == 'cosolute':
                self.n_cosolutes+=1
            elif card.type == 'small molecule':
                self.n_small_molecules+=1
            elif card.type == 'lipid':
                self.n_lipids+=1
            elif card.type == 'peptide':
                self.n_peptides+=1
            elif card.type == 'protein':
                self.n_proteins+=1
            elif card.type == 'dna':
                self.n_dnas+=1
            elif card.type == 'rna':
                self.n_rnas+=1
            self.n_cards +=1

        pass

    def draw(self, name='all'):

        if name=='all':

            output = list(self.cards.values())

            self.card = {}
            self.n_ions = 0
            self.n_waters = 0
            self.n_cosolutes = 0
            self.n_small_molecules = 0
            self.n_lipids = 0
            self.n_peptides = 0
            self.n_proteins = 0
            self.n_dnas = 0
            self.n_rnas = 0
            self.n_cards = 0

        else:

            output = self.card.pop(name)

            if card.type == 'ion':
                self.n_ions-=1
            elif card.type == 'water':
                self.n_waters-=1
            elif card.type == 'cosolute':
                self.n_cosolutes-=1
            elif card.type == 'small molecule':
                self.n_small_molecules+=1
            elif card.type == 'lipid':
                self.n_lipids-=1
            elif card.type == 'peptide':
                self.n_peptides-=1
            elif card.type == 'protein':
                self.n_proteins-=1
            elif card.type == 'dna':
                self.n_dnas-=1
            elif card.type == 'rna':
                self.n_rnas-=1

            self.n_cards-=1

            raise NotImplementedError

        return output

