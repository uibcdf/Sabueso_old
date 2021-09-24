import xmltodict
import urllib
import requests
from sabueso.native.evidence import Evidence, JournalArticleReference, DatabaseReference
from sabueso.native import UniProtKBEntry
from sabueso.tools.database.UniProtKB import is_accessible as UniProtKB_is_accessible
from sabueso.tools.string.uniprot_id import to_uniprotkb_dict
from collections import OrderedDict

def get(record, entry):

    output = Evidence()

    aux = DatabaseReference()
    aux.name = 'UniProtKB'
    aux.id = entry['accession'][0]

    output.references.append(aux)

    if type(record)==str:
        output.value = record
    elif type(record)==list:
        output.value = record
    elif type(record)==OrderedDict:
        if '#text' in record:
            output.value = record['#text']
            with_db_evidence = True
        else:
            print(type(record))
            print(record)
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
        else:
            print(type(record))
            print(record)
            raise ValueError('Evidence without known references')
    else:
        print(type(record))
        print(record)
        raise ValueError('Unknown record')

    return output

def to_sabueso_UniProtKBEntry(string):

    uniprotkb_dict = to_uniprotkb_dict(string)
    entry = uniprotkb_dict['uniprot']['entry']

    uniprot = UniProtKBEntry()

    uniprot.dataset = _get_evidence(['@dataset'], entry)
    uniprot.created = _get_evidence(['@created'], entry)
    uniprot.modified = _get_evidence(['@modified'], entry)
    uniprot.version = _get_evidence(['@version'], entry)

    uniprot.accession = _get_evidence(['accession'], entry)

    uniprot.name = _get_evidence(['name'], entry)

    # protein
    protein = uniprot.protein
    db_protein = entry['protein']
    ## recommendedName
    if 'recommendedName' in db_protein:
        recommendedName = protein.recommendedName
        db_recommendedName = db_protein.pop('recommendedName')
        ### fullName
        if 'fullName' in db_recommendedName:
            db_fullName = db_recommendedName.pop('fullName')
            recommendedName.fullName = get(db_fullName, entry)
        ### shortName
        if 'shortName' in db_recommendedName:
            db_shortName = db_recommendedName.pop('shortName')
            if type(db_shortName)==list:
                recommendedName.shortName = []
                while db_shortName:
                    recommendedName.shortName.append(get(db_shortName.pop(), entry))
            else:
                recommendedName.shortName = get(db_shortName, entry)
        ### ecNumber
        if 'ecNumber' in db_recommendedName:
            recommendedName.ecNumber = get(db_recommendedName.pop('ecNumber'), entry)
        ### finnal check
        if len(db_recommendedName)>0:
            raise ValueError('Unknown records in uniprot>entry>protein>recommendedName')

    ## alternativeName
    if 'alternativeName' in db_protein:
        alternativeName = protein.alternativeName
        db_alternativeName = db_protein.pop('alternativeName')
        if type(db_alternativeName)==list:
            alternativeName= []
            while db_alternativeName:
                alternativeName.append(get(db_alternativeName.pop(), entry))
            else:
                recommendedName.shortName = get(db_shortName, entry)



    for aux in entry['protein']['alternativeName']:
        for key, value in aux.items():
            uniprot.protein.alternativeName.append(_evidence(value, entry))

    return uniprot

