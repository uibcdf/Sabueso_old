import xmltodict
import urllib
import requests
from sabueso.native.evidence import Evidence, JournalArticleReference, DatabaseReference
from sabueso.native import UniProtKBEntry
from sabueso.tools.database.UniProtKB import is_accessible as UniProtKB_is_accessible
from sabueso.tools.string.uniprot_id import to_uniprotkb_dict

def _evidence(record, entry):

    output = Evidence()

    aux = DatabaseReference()
    aux.name = 'UniProtKB'
    aux.id = entry['accession'][0]

    output.references.append(aux)

    if '#text' in record:
        output.value = record['#text']
    else:
        raise ValueError('Evidence without known value')

    if '@evidence' in record:
        evidence_number_in_db = int(record['@evidence'])
        evidence_from_db = entry['evidence'][evidence_number_in_db-1]
        if int(evidence_from_db['@key'])!=evidence_number_in_db:
            raise ValueError('Evidence number does not match evidence @key')
        if 'source' in evidence_from_db:
            if 'dbReference' in evidence_from_db['source']:
                aux = DatabaseReference()
                aux.name = evidence_from_db['source']['dbReference']['@type']
                aux.id = evidence_from_db['source']['dbReference']['@id']
                output.references.append(aux)

    return output

def to_sabueso_UniProtKBEntry(string):

    uniprotkb_dict = to_uniprotkb_dict(string)
    entry = uniprotkb_dict['uniprot']['entry']

    uniprot = UniProtKBEntry()

    uniprot.dataset = entry['@dataset']
    uniprot.created = entry['@created']
    uniprot.modified = entry['@modified']
    uniprot.version = entry['@version']

    uniprot.accession = entry['accession']

    uniprot.name = entry['name']

    # protein
    protein = entry['protein']
    recommendedName = protein['recommendedName']
    uniprot.protein.recommendedName.fullName = _evidence(recommendedName['fullName'], entry)
    uniprot.protein.recommendedName.ecNumber = _evidence(recommendedName['ecNumber'], entry)
    #for aux in protein['alternativeName']:
    #    for key, value in aux.items():
    #        self.protein.alternativeName.append(_evidence(value, entry['evidence']))

    return uniprot
