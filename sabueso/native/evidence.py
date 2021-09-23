class Evidence():

    def __init__(self):

        self.value = None
        self.references = []

class JournalArticleReference():

    def __init__(self):

        self.type = 'journal article'
        self.year = None
        self.journal = None
        self.volume = None
        self.first_page = None
        self.last_page = None
        self.title = None
        self.authors = None

class DatabaseReference():

    def __init__(self):

        self.type = 'database'
        self.name = None
        self.id = None


