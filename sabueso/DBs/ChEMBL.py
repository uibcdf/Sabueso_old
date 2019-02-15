def data_to_protein(protein=None):

    chembl_id = protein.card['ChEMBL']

    from chembl_webresource_client.new_client import client
    result = client.target.filter(target_chembl_id__in=chembl_id)[0]

    # Name
    protein.card['Name'].append(result['pref_name'])

    # Type
    protein.card['Type'].append(result['target_type'])

    # Organism
    protein.card['Organism'].append(result['organism'])

    # ChEMBL
    protein.card['ChEMBL'].append(result['target_chembl_id'])

    ##### components?
    if len(result['target_components'])>1:
        print('La proteína tiene más de un target_components y no se que es.')

    for xref in result['target_components'][0]['target_component_xrefs']:

        src_db = xref['xref_src_db']
        id_db = xref['xref_id']

    # PDB
        if src_db == 'PDBe':
            protein.card['PDB'].append(id_db)

    # UniProt
        elif src_db == 'UniProt':
            protein.card['UniProt'].append(id_db)

    # IntAct
        elif src_db == 'IntAct':
            protein.card['IntAct'].append(id_db)

    # InterPro
        elif src_db == 'InterPro':
            protein.card['InterPro'].append(id_db)

    # Pfam
        elif src_db == 'Pfam':
            protein.card['Pfam'].append(id_db)

    del(result,client)

