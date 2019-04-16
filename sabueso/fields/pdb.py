from copy import deepcopy as _deepcopy

pdb_card = {
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
    'Ligand': {}
}

bioAssemblies_card = {
    'Name': None,
    'Chains': None
}

group_card = {
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

chain_card = {
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

entity_card = {
    'Description' : None,
    'Type' : None,
    'Sequence': None,
    'UniProt': None,
    'Chains': []
}

ligand_card = {
    'Name': None,
    'Chemical Id': None,
    'Residue Name': None,
    'Name':None,
    'Entity':None,
    'Chains':None,
    'ChEMBL':None,
    'InChIKey':None,
}

def equal_pdb_cards(card1=None, card2=None):
    return card1['Id']==card2['Id']

def merge_pdb_cards(cards=None):

    return cards[0]

def pdb_cards_depuration(cards=None):

    num_cards = len(cards)
    pairs_equal=[]
    for ii in range(num_cards):
        for jj in range(ii+1,num_cards):
            if equal_pdb_cards(cards[ii],cards[jj]):
                pairs_equal.append([ii,jj])

    result=[]
    while pairs_equal:
        bb=pairs_equal.pop(0)
        cc=[]
        for ii in range(len(pairs_equal)):
            if set.intersection(set(bb),set(pairs_equal[ii])):
                bb=list(set.union(set(bb),set(pairs_equal[ii])))
                cc.append(ii)
        aa2=[]
        for ii in range(len(pairs_equal)):
            if ii not in cc:
                aa2.append(pairs_equal[ii])
        pairs_equal=aa2
        result.append(bb)

    pairs_equal=result

    list_depurated=[]

    for ii in pairs_equal:
        list_depurated.append(merge_pdb_cards([cards[jj] for jj in ii]))

    flat_pairs_equal = [item for sublist in pairs_equal for item in sublist]

    for ii in range(num_cards):
        if ii not in flat_pairs_equal:
            list_depurated.append(cards[ii])

    return list_depurated

