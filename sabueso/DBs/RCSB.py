# There are already some opensource tools to extract information
# from the RCSB:
# https://github.com/williamgilpin/pypdb
# https://github.com/biopython/biopython

# We start using PyPDB and mmtf-python

import pypdb as _pypdb
from copy import deepcopy as _deepcopy
import urllib as _urllib
import mmtf as _mmtf

def _get_seq_from_fasta_rcsb(pdb=None,chainId=None):
    url = 'https://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=fastachain&compression=NO&structureId='+pdb+'&chainId='+chainId
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    fasta_txt = response.read().decode('utf-8')
    return ''.join(fasta_txt.split('\n')[1:])

def card_pdb(pdb=None, card=None):

    if card is None:
        from sabueso.fields.pdb import _pdb_dict
        tmp_card = _deepcopy(_pdb_dict)
        del(_pdb_dict)
    else:
        tmp_card = _deepcopy(card)

    if pdb is not None:
        tmp_card['Id'].append(pdb)

    pdb_id=tmp_card['Id']

    # PyPDB:

    _pdb_description = pypdb.describe_pdb('4ZPR')
    _all_info = pypdb.get_all_info('4ZPR')
    _entity_info = pypdb.get_entity_info('4ZPR')
    _ligands_info = pypdb.get_ligands('4ZPR')

    ### Describe_pdb

    _tmp_card['Method']=_pdb_description['expMethod']
    _tmp_card['Title']=_pdb_description['title']
    _tmp_card['Resolution']=_pdb_description['resolution']
    _tmp_card['Id']=_pdb_description['structureID']
    for tmp_pdb in _pdb_description['relatedPDB']:
       _tmp_card['Related PDBs'].append(tmp_pdb['@pdbId'])
    _tmp_card['Number Entities']=_pdb_description['nr_entities']

    ### All_info
    from sabueso.fields.pdb import entity_dict as _entity_dict
    for tmp_data in _all_info['polymer']:
        tmp_entity = _deepcopy(_entity_dict)
        tmp_entity['Type']=tmp_data['@type']
        tmp_entity['Length']=tmp_data['@length']
        tmp_entity['Index']=tmp_data['@entityNr']
        tmp_entity['Weight']=tmp_data['@weight']
        for tmp_chain in tmp_data['chain']:
            tmp_entity['Chain'].append(tmp_chain['@id'])
            tmp_entity['Number Chains']+=1
        tmp_entity['Organism Scientific']=tmp_data['Taxonomy']['@name']
        tmp_entity['Description']=tmp_data['polymerDescription']['@description']
        if tmp_entity['Type']=='protein':
            tmp_entity['Alternative Name']=tmp_data['synonym']['@name'].split(', ')
            tmp_entity['Name']=tmp_data['macroMolecule']['@name']
            tmp_entity['UniProt']=tmp_data['macroMolecule']['Accesion']['@id']
            tmp_entity['Begin']=int(tmp_data['fragment'].replace('UNP residues ','').split('-')[0])
            tmp_entity['End']=int(tmp_data['fragment'].replace('UNP residues ','').split('-')[1])
        elif tmp_entity['Type']=='dna':
            tmp_entity['DNA Details']=tmp_data['details']['@desc']
        tmp_card['Entity'][tmp_entity['Index']-1]=tmp_entity
        del(tmp_entity)
    del(_entity_dict)

    ### Entity_info

    tmp_card['bioAssemblies']=_entity_info['bioAssemblies']

    ### Ligands_info

    if _ligands_info['ligandInfo'] is None:
        tmp_card['Ligand']=None
    else:
        from sabueso.fields.pdb import ligand_dict as _ligand_dict
        tmp_data = _ligands_info['ligandInfo']['ligand']
        tmp_ligand = _deepcopy(_ligand_dict)
        tmp_ligand['Residue Name']=tmp_data['@chemicalID']
        tmp_ligand['Chemical Id']=tmp_data['@chemicalID']
        tmp_ligand['Weight']=tmp_data['@molecularWeight']
        tmp_ligand['Name']=tmp_data['chemicalName']
        tmp_ligand['Formula']=tmp_data['formula']
        tmp_ligand['InChI']=tmp_data['InChI']
        tmp_ligand['InChIKey']=tmp_data['InChIKey']
        tmp_ligand['Smile']=tmp_data['smiles']
        tmp_card['Ligand'][tmp_ligand['Residue Name']]=tmp_ligand
        del(tmp_ligand,_ligand_dict)

    del(_all_info,_pdb_description,_entity_info,_ligands_info)

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


    _mmtf_pdb = _fetch(pdb_id)
    from sabueso.fields.pdb import _mmtf_group_dict

    _tmp_mmtf_groups = _deepcopy(_mmtf_group_dict)
    _tmp_mmtf_groups['Index']=_mmtf_pdb.group_id_list
    _tmp_mmtf_groups['Type']=[_mmtf_pdb.group_list[ii] for ii in _mmtf_pdb.group_type_list]
    _tmp_mmtf_groups['Sequence']=[ii['singleLetterCode'] for ii in _tmp_mmtf_groups['Type']]
    _tmp_dssp = [_sec_struct_codes[ii] for ii in _mmtf_pdb.sec_struct_list]
    _tmp_mmtf_groups['Secondary Structure DSSP']=_tmp_dssp
    tmp_card['Secondary Structure ABC']=[_dssp_to_abc[ii] for ii in _tmp_dssp]
    _tmp_mmtf_groups['Chain Index']=_tmp_dssp

    del(_mmtf_pdb, _tmp_dssp)
