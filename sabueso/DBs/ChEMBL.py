def card_protein(chembl=None, card=None):

    if card is None:
        from sabueso.fields.protein import _protein_dict
        tmp_card = _protein_dict.copy()
        tmp_card['ChEMBL'].append(chembl)
        del(_protein_dict)
    else:
        tmp_card = card.copy()

    chembl_id=tmp_card['ChEMBL'][0]

    from chembl_webresource_client.new_client import new_client as client
    result = client.target.filter(target_chembl_id__in=chembl_id)[0]

    # Name
    tmp_card['Name'].append(result['pref_name'])

    # Type
    tmp_card['Type'].append(result['target_type'])

    # Organism
    tmp_card['Organism Scientific'].append(result['organism'])

    # ChEMBL
    tmp_card['ChEMBL'].append(result['target_chembl_id'])

    ##### components?
    if len(result['target_components'])>1:
        print('La proteína tiene más de un target_components y no se que es.')

    for xref in result['target_components'][0]['target_component_xrefs']:

        src_db = xref['xref_src_db']
        id_db = xref['xref_id']

    # PDB
        if src_db == 'PDBe':
            if id_db not in tmp_card['PDB'].keys():
                from sabueso.fields.pdb import _pdb_dict
                tmp_pdb = _pdb_dict.copy()
                tmp_pdb['id']=id_db
                tmp_card['PDB'][id_db]=tmp_pdb

    # UniProt
        elif src_db == 'UniProt':
            tmp_card['UniProt'].append(id_db)

    # IntAct
        elif src_db == 'IntAct':
            tmp_card['IntAct'].append(id_db)

    # InterPro
        elif src_db == 'InterPro':
            tmp_card['InterPro'].append(id_db)

    # Pfam
        elif src_db == 'Pfam':
            tmp_card['Pfam'].append(id_db)

    del(result,client)

    return tmp_card
