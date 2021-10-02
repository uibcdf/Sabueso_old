from collections import OrderedDict
from evidence import Evidence

def get_uniprot(item, entity='all'):

    evidence = Evidence()
    accession = item['uniprot']['entry']['accession'][0]
    evidence.value = accession
    evidence.add_UniProtKB(id=accession)

    return evidence

