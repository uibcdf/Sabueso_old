from evidency import Evidence

form_name='uniprotkb.XMLDict'

is_form={
}

def this_dict_is_a_uniprotkb_XMLDict(item):

    return list(item.keys())==['uniprot']

def _get(record, entry):

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

def _add_reference_to_evidence(evidence, evidence_in_db):

    if 'source' in evidence_from_db:
        if 'dbReference' in evidence_from_db['source']:
            dbtype = evidence_from_db['source']['dbReference']['@type']
            dbid = evidence_from_db['source']['dbReference']['@id']

            if dbtype=='UniProtKB':
                evidence.add_UniProtKB(id=dbid)
            elif dbtype=='PubMed':
                evidence.add_PubMed(id=dbid)
            elif dbtype=='DOI':
                evidence.add_PubMed(id=dbid)
            else:
                raise ValueError('Uknown source')

def get_n_entities(item):

    return 1

def get_entity_names(item):

    output = []

    entity_name = Evidence()

    fullName = item['uniprot']['entry']['recommendedName']['fullName']

    if type(fullName)==str:
        entity_name.value=fullName
    elif type(fullName)==OrderedDict:
        if '#text' in fullName:
            entity_name.value = fullName['#text']
        if '@evidence' in fullName:
            evidence_number_in_db = fullName['@evidence']
            evidence_from_db = item['uniprot']['entry']['evidence'][int(evidence_number_in_db)-1]
            if int(evidence_from_db['@key'])!=evidence_number_in_db:
                raise ValueError('Evidence number does not match evidence @key')
            _add_reference_to_evidence(entity_name, evidence_from_db)

    output.append(entity_name)

    return output

def get_card(entity_name):

    pass

def get_cards(entity_names='all'):

    output = []

    pass

