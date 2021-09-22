import xmltodict
import urllib
from sabueso.native import Evidence
from sabueso.native import UniProtKBEntry
from sabueso.tools.database.UniProtKBEntry 

def _evidence(entry, evidences):

    evidence_number_in_db = entry['@evidence']
    evidence_from_db = evidences[int(evidence_number_in_db)-1]
    if evidence_from_db['@key']!=evidence_number_in_db:
        raise ValueError('Evidence number does not match evidence @key')

    evidence = Evidence(database='UniProtKB')
    evicence.value = entry['#text']
    evicence.source_type = evidence_from_db['dbReference']['@type']
    evicence.source_ref = evidence_from_db['dbReference']['@id']

def to_sabueso_UniProtKBEntry(string):

    url = 'http://www.uniprot.org/uniprot/'+string+'.xml'
    headers = ('user-agent': 'Python lib at https://github.com/uibcdf/sabueso || prada.gracia@gmail.com')
    r = requests.get(url, headers=headers, timeout=5)
    if not r.status_code == requests.codes.ok:

    dict_result = xmltodict.parse(r.text)
    entry = dict_result['uniprot']['entry']

    uniprot = UniProtKBEntry()

    uniprot.dataset = entry['@dataset']
    uniprot.created = entry['@created']
    uniprot.modified = entry['@modified']
    uniprot.version = entry['@version']

    self.accession = entry['accession']

    self.name = entry['name']

    # protein
    protein = entry['protein']
    recommendedName = protein['recommendedName']
    self.protein.recommendedName.fullName = _evidence(recommendedName['fullName'], dd['evidence'])
    self.protein.recommendedName.ecNumber = _evidence(recommendedName['ecNumber'], dd['evidence'])
    for aux in protein['alternativeName']:
        for key, value in aux.items():
            self.protein.alternativeName.append(_evidence(value, dd['evidence']))

