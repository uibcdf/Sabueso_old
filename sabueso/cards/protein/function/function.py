from sabueso.cards.card import Card
from copy import deepcopy
from pandas import DataFrame

class FunctionCard(Card):

    def __init__(self):

        super().__init__()

        self.protein_name = None
        self.organism_common_name = None
        self.protein_key_name = None
        self.protein_uniprot_id = None

        self.uniprot_function = None
        self.notes = []
        self.references = []

    def to_pandas_DataFrame(self, with_evidences=True):

        aux_dict = {}
        aux_dict['protein_name']=[self.protein_name]
        aux_dict['organism_common_name']=[self.organism_common_name]
        aux_dict['protein_key_name']=[self.protein_key_name]
        aux_dict['protein_uniprot_id']=[self.protein_uniprot_id]
        aux_dict['uniprot_function']=[self.uniprot_function]
        aux_dict['notes']=[self.notes]
        aux_dict['references']=[self.references]

        df = DataFrame(aux_dict)

        return df

    def to_jupyter_notebook(self, filename=None):

        import nbformat as nbf
        from .notebook import notebook

        nb = notebook(self)

        if filename is None:
            filename = f'{self.protein_key_name.value}_function.ipynb'

        with open(filename, 'w') as fff:
            nbf.write(nb, fff)

        return filename

    def show(self):

        import nbformat as nbf
        from .notebook import notebook

        nb = notebook(self)

        return nb

    def __repr__(self):

        return f'<ProteinFunctionCard: {self.protein_key_name}>'

