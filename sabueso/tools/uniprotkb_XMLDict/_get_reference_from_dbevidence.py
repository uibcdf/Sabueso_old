import evidence as evi

def _get_reference_from_dbevidence(evidence_number_in_db, item):

    ref = None

    aux_index = evidence_number_in_db-1

    evidence_in_db = item['uniprot']['entry']['evidence'][aux_index]

    if int(evidence_in_db['@key'])!=evidence_number_in_db:
        raise ValueError('Evidence number not matching the index in the OrderedDict object')

    if 'source' in evidence_in_db:
        if 'dbReference' in evidence_in_db['source']:

            dbtype = evidence_in_db['source']['dbReference']['@type']
            dbid = evidence_in_db['source']['dbReference']['@id']

            if dbtype=='UniProtKB':
                ref = evi.reference({'database':'UniProtKB', 'id':dbid})
            elif dbtype=='PubMed':
                ref = evi.reference({'database':'PubMed', 'id':dbid})
            elif dbtype=='DOI':
                ref = evi.reference({'database':'DOI', 'id':dbid})
            elif dbtype=='PROSITE-ProRule':
                ref = evi.reference({'database':'PROSITE_ProRule', 'id':dbid})
            elif dbtype=='PDB':
                ref = evi.reference({'database':'PDB', 'id':dbid})
            elif dbtype=='SAM':
                if dbid=='MobiDB-lite':
                    from .get_uniprot import get_uniprot
                    ref_uniprot=get_uniprot(item)
                    ref = evi.reference({'database':'MobiDB', 'id':ref_uniprot.value})
                else:
                    raise ValueError(f'Unknown SAM source {dbtype} in evidence {evidence_in_db}')
            else:
                raise ValueError(f'Unknown source {dbtype} in evidence {evidence_in_db}')

    return ref

