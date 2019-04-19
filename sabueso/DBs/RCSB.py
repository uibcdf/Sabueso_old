# We start with mmtf-python and some APIs from DBs
import urllib as _urllib
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

    # molmodel has a method to create a pdb object coming from the mmtf file from RCSB
    from molmodel.io.to_pdb import from_pdb_id as _pdb_from_pdb_id

    tmp_pdb=_pdb_from_pdb_id(pdb.id)

    list_attributes = ['method', 'resolution', 'title', 'deposition_date', 'unit_cell',
                       'bioassembly', 'chain', 'segment', 'group', 'atom', 'bond', 'num_models',
                       'num_bioassemblies', 'num_chains', 'num_entities', 'num_segments',
                       'num_groups', 'num_atoms', 'num_bonds', 'ion', 'water', 'small_molecule',
                       'protein', 'peptide', 'dna', 'rna', 'num_ions', 'num_waters',
                       'num_small_molecules', 'num_proteins', 'num_peptides', 'num_dnas',
                       'num_rnas', 'coordinates']


    for pdb_attribute in list_attributes:
        value = getattr(tmp_pdb, pdb_attribute)
        setattr(pdb,pdb_attribute,value)

    pass

