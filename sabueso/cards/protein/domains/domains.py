from sabueso.cards.card import Card
from copy import deepcopy
from pandas import DataFrame

domains_dict = {

        'protein_name':None,
        'protein_keyname':None,
        'protein_uniprot_id':None,

        'references':[],
        'domain':[],
        'notes':None,

        'interpro_id':None,
        'panther_id':None,
        'pfam_id':None,
        'supfam_id':None,
        'prosite_id':None,

        }

def is_domains_dict(item):

    output = False

    if type(item) is dict:
        if set(domains_dict)==set(item):
            output = True

    return output

class DomainsCard(Card):

    def __init__(self, item=None):

        super().__init__()

        self.card_type = 'domains'

        if is_domains_dict(item):
            for key, value in item.items():
                setattr(self,key,value)
        else:
            for key, value in domains_dict.items():
                setattr(self, key, value)

    def to_dict(self):

        output = deepcopy(domains_dict)
        for key in output:
            output[key]=getattr(self, key)

        return output

    def to_pandas_DataFrame(self, with_evidences=True):

        aux_dict = self.to_dict()
        for key in aux_dict:
            aux_dict[key]=[aux_dict[key]]

        if not with_evidences:
            for key in aux_dict:
                try:
                    aux_dict[key]=aux_dict[key][0].value
                except:
                    continue

        df = DataFrame(aux_dict, index =[self.begin+'-'+self.end])

        return df

    def __repr__(self):

        return f'<DomainsCard: {len(self.domain)} domains>'

