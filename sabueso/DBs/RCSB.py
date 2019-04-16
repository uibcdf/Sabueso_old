# We start  mmtf-python and some APIs from DBs

from copy import deepcopy as _deepcopy
import urllib as _urllib
import mmtf as _mmtf
import json as _json

#MMTF
#https://github.com/rcsb/mmtf/blob/master/spec.md#secstructlist
_sec_struct_codes = {0 : "I", #pi helix
                     1 : "S", # bend
                     2 : "H", # alpha helix
                     3 : "E", # extended
                     4 : "G", # 3-10 helix
                     5 : "B", # bridge
                     6 : "T", # turn
                     7 : "C", # coil
                     -1: "X"} # undefined

_dssp_to_abc = {"I" : "c", # coil
                "S" : "c",
                "H" : "a", # helix
                "E" : "b", # sheet
                "G" : "c",
                "B" : "b",
                "T" : "c",
                "C" : "c",
                "X" : "X"} # undefined

def _pdb_to_uniprot_SIFTS(pdb=None):

    url = 'http://www.ebi.ac.uk/pdbe/api/mappings/uniprot/'+pdb
    request = _urllib.request.Request(url)
    response = _urllib.request.urlopen(request)
    response_txt = response.read().decode('utf-8')
    sifts_api_dict = _json.loads(response_txt)
    pdbid = list(sifts_api_dict.keys())[0]
    result=[]
    for uniprotid in sifts_api_dict[pdbid]['UniProt'].keys():
        for mapp in sifts_api_dict[pdbid]['UniProt'][uniprotid]['mappings']:
            tmp_dict={}
            tmp_dict['uniprot']=uniprotid
            tmp_dict['entity_id']=mapp['entity_id']
            tmp_dict['chain_id']=mapp['chain_id']
            tmp_dict['pdb_start']=mapp['start']['residue_number']
            tmp_dict['pdb_end']=mapp['end']['residue_number']
            tmp_dict['uniprot_start']=mapp['unp_start']
            tmp_dict['uniprot_end']=mapp['unp_end']
            result.append(tmp_dict)
    del(url, request, response, response_txt, sifts_api_dict, pdbid, uniprotid, mapp)

    return result

def _data_from_chemid(chem_id=None):

    url = 'https://www.ebi.ac.uk/pdbe/api/pdb/compound/summary/'+chem_id
    request = _urllib.request.Request(url)
    response = _urllib.request.urlopen(request)
    response_txt = response.read().decode('utf-8')
    ligand_api_dict = _json.loads(response_txt)
    inchikey = ligand_api_dict[chem_id][0]["inchi_key"]
    chemblid = ligand_api_dict[chem_id][0]["chembl_id"]
    return inchikey, chemblid

def _ligand_from_pdb(pdb=None):

    from sabueso.fields.pdb import ligand_card as _ligand_card
    ligands={}
    url = 'https://www.ebi.ac.uk/pdbe/api/pdb/entry/ligand_monomers/'+pdb
    request = _urllib.request.Request(url)
    response = _urllib.request.urlopen(request)
    response_txt = response.read().decode('utf-8')
    ligand_api_dict = _json.loads(response_txt)
    pdbid = list(ligand_api_dict.keys())[0]
    for tmp_ligand in ligand_api_dict[pdbid]:
        tmp_dict=_deepcopy(_ligand_card)
        tmp_dict['Name']=tmp_ligand['chem_comp_name']
        tmp_dict['Residue Name']=tmp_ligand['chem_comp_id']
        tmp_dict['Entity']=tmp_ligand['chem_comp_id']
        tmp_dict['Chemical Id']=tmp_ligand['chem_comp_id']
        tmp_dict['InChIKey'],tmp_dict['ChEMBL']=_data_from_chemid(tmp_dict['Chemical Id'])
        ligands[tmp_dict['Chemical Id']]=tmp_dict
        del(tmp_dict)
    return ligands

def _get_seq_from_fasta_rcsb(pdb=None,chainId=None):

    url = 'https://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=fastachain&compression=NO&structureId='+pdb+'&chainId='+chainId
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    fasta_txt = response.read().decode('utf-8')
    return ''.join(fasta_txt.split('\n')[1:])

def pdb_card(pdb=None, card=None):

    if card is None:
        from sabueso.fields.pdb import pdb_card as _pdb_card
        tmp_card = _deepcopy(_pdb_card)
        del(_pdb_card)
    else:
        tmp_card = _deepcopy(card)

    if pdb is not None:
        tmp_card['Id']=pdb

    pdb_id=tmp_card['Id']

    _mmtf_pdb = _mmtf.fetch(pdb_id)
    from sabueso.fields.pdb import bioAssemblies_card as _bioAssemblies_card
    from sabueso.fields.pdb import group_card as _group_card
    from sabueso.fields.pdb import chain_card as _chain_card
    from sabueso.fields.pdb import entity_card as _entity_card

    tmp_card['MMTF']=_mmtf_pdb
    tmp_card['Method']=_mmtf_pdb.experimental_methods
    tmp_card['Title']=_mmtf_pdb.title
    tmp_card['Resolution']=_mmtf_pdb.resolution
    tmp_card['Deposition Date']=_mmtf_pdb.deposition_date
    tmp_card['Unit Cell']=_mmtf_pdb.unit_cell
    tmp_card['Number Entities']=len(_mmtf_pdb.entity_list)
    tmp_card['Number Models']=_mmtf_pdb.num_models
    tmp_card['Number bioAssemblies']=len(_mmtf_pdb.bio_assembly)
    tmp_card['Number Chains']=_mmtf_pdb.num_chains
    tmp_card['Number Groups']=_mmtf_pdb.num_groups

    ## bioAssemblies

    for ii in _mmtf_pdb.bio_assembly:
        _tmp_item = _deepcopy(_bioAssemblies_card)
        _tmp_item['Name']=ii['name']
        _tmp_item['Chains']=ii['transformList'][0]['chainIndexList']
        tmp_card['bioAssembly'][ii['name']]=_tmp_item
        del(_tmp_item)

    ## Groups

    for ii in range(_mmtf_pdb.num_groups):
        _tmp_item = _deepcopy(_group_card)
        _tmp_item['Id'] = _mmtf_pdb.group_id_list[ii]
        _tmp_group = _mmtf_pdb.group_list[_mmtf_pdb.group_type_list[ii]]
        _tmp_item['Name'] = _tmp_group['groupName']
        _tmp_item['Atom Name List'] = _tmp_group['atomNameList']
        _tmp_item['Element List'] = _tmp_group['elementList']
        _tmp_item['Bond Order List'] = _tmp_group['bondOrderList']
        _tmp_item['Bond Atom List'] = _tmp_group['bondAtomList']
        _tmp_item['Formal Charge List'] = _tmp_group['formalChargeList']
        _tmp_item['Letter Code'] = _tmp_group['singleLetterCode']
        _tmp_item['Type'] = _tmp_group['chemCompType']
        tmp_card['Group'][ii]=_tmp_item
        del(_tmp_item)

    ## Chains

    ind_start=0
    _tmp_dssp = [_sec_struct_codes[ii] for ii in _mmtf_pdb.sec_struct_list]
    for ii in range(_mmtf_pdb.num_chains):
        _tmp_item = _deepcopy(_chain_card)
        _tmp_item['Index'] = ii
        _tmp_item['Id'] = _mmtf_pdb.chain_id_list[ii]
        _tmp_item['Name'] = _mmtf_pdb.chain_name_list[ii]
        _tmp_item['Groups'] = list(range(ind_start,ind_start+_mmtf_pdb.groups_per_chain[ii]))
        ind_start+=_mmtf_pdb.groups_per_chain[ii]
        tmp_seq = [tmp_card['Group'][ii]['Letter Code'] for ii in _tmp_item['Groups']]
        _tmp_item['Sequence'] = ''.join(tmp_seq)
        _aux_ss =[_tmp_dssp[jj] for jj in _tmp_item['Groups']]
        _tmp_item['Secondary Structure DSSP'] =''.join(_aux_ss)
        _tmp_item['Secondary Structure ABC'] = ''.join([_dssp_to_abc[jj] for jj in _aux_ss])
        tmp_card['Chain'][_mmtf_pdb.chain_id_list[ii]]=_tmp_item
        del(_tmp_item,tmp_seq,_aux_ss)
    del(ind_start,_tmp_dssp)

    _tmp_pdb2unip = _pdb_to_uniprot_SIFTS(pdb=pdb_id)
    for _tmp_item in _tmp_pdb2unip:
        _tmp_chain =tmp_card['Chain'][_tmp_item['chain_id']]
        _tmp_chain['UniProt'] = _tmp_item['uniprot']
        _tmp_chain['Entity'] = _tmp_item['entity_id']
        _tmp_chain['PDB_start'] = _tmp_item['pdb_start']
        _tmp_chain['PDB_end'] = _tmp_item['pdb_end']
        _tmp_chain['UniProt_start'] = _tmp_item['uniprot_start']
        _tmp_chain['UniProt_end'] = _tmp_item['uniprot_end']
    del(_tmp_item,_tmp_pdb2unip)

    ## Entities

    for _tmp_item in _mmtf_pdb.entity_list:
        _tmp_entity = _deepcopy(_entity_card)
        _tmp_entity['Description']=_tmp_item['description']
        _tmp_entity['Type']=_tmp_item['type']
        _tmp_entity['Sequence']=_tmp_item['sequence']
        _tmp_entity['Chains']=[_mmtf_pdb.chain_id_list[ii] for ii in _tmp_item['chainIndexList']]
        if _tmp_entity['Type']=='polymer':
            _tmp_entity['UniProt']=tmp_card['Chain'][_tmp_entity['Chains'][0]]['UniProt']
            tmp_card['Entity'][_tmp_entity['UniProt']]=_tmp_entity
        else:
            tmp_card['Entity'][_tmp_entity['Description']]=_tmp_entity
        del(_tmp_entity)
    del(_tmp_item)



    tmp_card['Ligand']=_ligand_from_pdb(pdb=pdb_id)
    for ii in tmp_card['Ligand']:
        ligand_name = tmp_card['Ligand'][ii]['Name']
        tmp_card['Ligand'][ii]['Chains']=tmp_card['Entity'][ligand_name]['Chains']
        tmp_card['Entity'][ii]=tmp_card['Entity'][ligand_name]
        del(tmp_card['Entity'][ligand_name])

    return tmp_card
