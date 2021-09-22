from copy import deepcopy

class RecommendedName():

    def __init__(self):

        self.fullName = None
        self.ecNumber = None

class Protein():

    def __init__(self):

        self.recommendedName = RecommendedName()
        self.alternativeName = []

class UniProtKBEntry():

    def __init__(self):

        self.dataset = None
        self.created = None
        self.modified = None
        self.version = None

        self.accession = []

        self.name = None

        self.protein = Protein()
