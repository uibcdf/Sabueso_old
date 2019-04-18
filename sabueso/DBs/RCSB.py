# We start with mmtf-python and some APIs from DBs

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

def _get_seq_from_fasta_rcsb(pdb=None,chainId=None):

    url = 'https://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=fastachain&compression=NO&structureId='+pdb+'&chainId='+chainId
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    fasta_txt = response.read().decode('utf-8')
    return ''.join(fasta_txt.split('\n')[1:])

def dress_pdb(pdb):

    tmp_mmtf = _mmtf.fetch(pdb.id)
    pdb.from_mmtf(tmp_mmtf)
    del(tmp_mmtf)
    pass

def pdb_card(pdb=None, card=None):

    pdb_id=pdb.id

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

    ## Entities

    entity_id=1
    for _tmp_item in _mmtf_pdb.entity_list:
        _tmp_entity = _deepcopy(_entity_card)
        _tmp_entity['Id'] = entity_id
        _tmp_entity['Description']=_tmp_item['description']
        _tmp_entity['Type']=_tmp_item['type']
        _tmp_entity['Sequence']=_tmp_item['sequence']
        _tmp_entity['Chains']=[_mmtf_pdb.chain_name_list[ii] for ii in _tmp_item['chainIndexList']]
        tmp_card['Entity'][entity_id]=_tmp_entity
        entity_id+=1
        del(_tmp_entity)
    del(_tmp_item)

    return tmp_card

