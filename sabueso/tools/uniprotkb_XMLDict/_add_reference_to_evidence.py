def _add_reference_to_evidence(evidence, evidence_in_db):

    if 'source' in evidence_in_db:
        if 'dbReference' in evidence_in_db['source']:

            dbtype = evidence_in_db['source']['dbReference']['@type']
            dbid = evidence_in_db['source']['dbReference']['@id']

            if dbtype=='UniProtKB':
                evidence.add_reference({'database':'UniProtKB', 'id':dbid})
            elif dbtype=='PubMed':
                evidence.add_reference({'database':'PubMed', 'id':dbid})
            elif dbtype=='DOI':
                evidence.add_reference({'database':'DOI', 'id':dbid})
            else:
                raise ValueError('Uknown source')

    pass

