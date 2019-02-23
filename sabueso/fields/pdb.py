
_pdb_dict = {
    'Id' : None,
    'Method' : None,
    'Resolution': None,
    'Title': None,
    'Deposition Date': None,
    'MMTF': None,
    'Unit Cell': None,
    'Number Entities': 0,
    'Number Chains': 0,
    'Number Models': 0,
    'Number bioAssemblies': 0,
    'Number Groups': 0,
    'bioAssembly': {},
    'Group': {},
    'Chain': {},
    'Entity': {},
    'Ligand': {},

}

_bioAssemblies_dict = {
    'Name': None,
    'Chains': None
}

_group_dict = {
    'Id': None,                 # Id from group_id_list MMTF
    'Name': None,               # groupName from MMTF
    'Atom Name List': None,     # atomNameList from MMTF
    'Element List': None,       # elementList from MMTF
    'Bond Order List': None,    # bondOrderList from MMTF
    'Bond Atom List': None,     # bondAtomList from MMTF
    'Formal Charge List': None, # formalChargeList from MMTF
    'Letter Code': None,        # singleLetterCode from MMTF
    'Type': None                # chemCompType from MMTF
}

_chain_dict = {
    'Index': None,
    'Id': None,
    'Name': None,
    'Type': None,
    'UniProt': None,
    'Entity': None,
    'PDB_start': None,
    'PDB_end': None,
    'UniProt_start': None,
    'UniProt_end': None,
    'Sequence': None,
    'Secondary Structure DSSP': None,
    'Secondary Structure ABC': None,
    'Groups' : None
}

_entity_dict = {
    'Description' : None,
    'Type' : None,
    'Sequence': None,
    'UniProt': None,
    'Chains': []
}

_ligand_dict = {
    'Name': None,
    'Chemical Id': None,
    'Residue Name': None,
    'Name':None,
    'Entity':None,
    'Chains':None,
    'ChEMBL':None,
    'InChIKey':None,
}


