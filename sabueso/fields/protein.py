
_ptm_dict ={
    'Modified Residues': {},
    'Cross-link': {}
}

_sequence_dict = {
    'Canonical': None,
    'FASTA': None,                 # Db: UniProt
    'Isoforms': {},              # Db: UniProt
    'PostTranslational Modifications' : _ptm_dict.copy(),           # Db: UniProt
    'Sequence Conflict' : {},          # Db: UniProt
    'Alternative Sequence' : {}           # Db: UniProt
}

_alternative_seq_dict = {
    'Begin': None,
    'End': None,
    'Description': None
}

_seq_conflict_dict = {
    'Begin': None,
    'End': None,
    'Description': None
}

_modified_res_dict = {
    'Begin': None,
    'End': None,
    'Description': None
}

_cross_link_dict = {
    'Begin': None,
    'End': None,
    'Description': None
}

_modified_res_dict = {
    'Begin': None,
    'End': None,
    'Description': None
}

_domain_dict = {
    'Name': None,
    'PROSITE-ProRule': None,
    'Begin': None,
    'End': None
}

_region_dict = {
    'Note': None,
    'Begin': None,
    'End': None
}

_motif_dict = {
    'Note': None,
    'Begin': None,
    'End': None
}

_chain_dict = {
    'Index' : None,
    'Description' : None,
    'Begin' : None,
    'End': None
}

_structure_dict = {
    'Chain': {},
    'Secondary': [],
    'Domain': {},               # Db: UniProt
    'Region': {},               # Db: UniProt
    'Motif': {}                 # Db: UniProt
}

_isoform_dict ={
    'UniProt': None,
    'Name': None,
    'Sequence': None,
    'FASTA': None
}

_experimental_evidences_dict={
    'Mutagenesis':{}
}

_mutagenesis_dict={
    'Begin':None,
    'End':None,
    'Description':None
}

_protein_dict   = {
    'Name' : [],                # Db: UniProt, ChEMBL
    'Full Name' : [],           # Db: UniProt
    'Short Name' : [],          # Db: UniProt
    'Alternative Name' : [],    # Db: UniProt
    'Type' : [],                # Db: ChEMBL
    'Organism' : [],            # Db: UniProt, ChEMBL
    'Organism Scientific' : [], # Db: UniProt, ChEMBL
    'Host' : [],                # Db: UniProt
    'Function' : [],            # Db: UniProt
    'Subunit Structure' : [],   # Db: Uniprot
    'Interactions' : [],        # Db: Uniprot
    'UniProt' : [],             # Db: UniProt, ChEMBL
    'Sequence': _sequence_dict.copy(),
    'Structure': _structure_dict.copy(),
    'Experimental Evidences': _experimental_evidences_dict.copy(),
    'ChEMBL' : [],              # Db: UniProt, ChEMBL
    'BioGRID' : [],             # Db: UniProt
    'ProteinModelPortal' : [],  # Db: UniProt
    'Swiss-Model' : [],         # Db: UniProt
    'DIP' : [],                 # Db: UniProt
    'ELM' : [],                 # Db: UniProt
    'IntAct' : [],              # Db: UniProt, ChEMBL
    'MINT' : [],                # Db: UniProt
    'BindingDB' : [],           # Db: UniProt,
    'InterPro' : [],            # Db: UniProt, ChEMBL
    'Pfam' : [],                # Db: UniProt, ChEMBL
    'ProDom' : [],              # Db: UniProt
    'PDB' : {},                 # Db: UniProt, ChEMBL
    'SUPFAM' : [],              # Db: UniProt
    'STRING' : [],              # Db: UniProt
    'iPTMnet' : [],              # Db: UniProt
    'PhosphoSitePlus' : []              # Db: UniProt
}


