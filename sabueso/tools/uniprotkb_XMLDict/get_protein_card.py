def get_protein_card(item):

    from sabueso.cards import ProteinCard
    from sabueso.cards import OrganismCard
    from .get_name import get_name
    from .get_short_name import get_short_name
    from .get_uniprot_entry_name import get_uniprot_entry_name
    from .get_alternative_names import get_alternative_names
    from .get_organism import get_organism
    from .get_host import get_host
    from .get_function import get_function
    from .get_canonical_sequence import get_canonical_sequence
    from .get_isoforms import get_isoforms
    from .get_uniprot import get_uniprot
    from .get_ec import get_ec
    from .get_dbreference import get_dbreference
    from .get_interactions import get_interactions
    from .get_subunit_structure import get_subunit_structure

    card = ProteinCard()

    # Names
    card.name = get_name(item)
    card.short_name = get_short_name(item)
    card.uniprot_entry_name = get_uniprot_entry_name(item)
    card.alternative_names = get_alternative_names(item)

    # Organism
    card.organism = get_organism(item, as_card=True)

    # Host
    card.host = get_host(item)

    # Function
    card.function = get_function(item)

    # Sequence
    card.sequence = get_canonical_sequence(item)

    # Isoforms
    card.isoforms = get_isoforms(item, as_cards=True)

    # Interactions
    card.interactions = get_interactions(item, as_cards=True)

    # Subunit structure
    card.subunit_structure = get_subunit_structure(item)

    # Chains
    card.chains = get_chains(item)

    # Databases
    card.uniprot =get_uniprot(item)
    card.ec = get_ec(item)
    card.chembl = get_dbreference(item, dbname='ChEMBL')
    card.biogrid = get_dbreference(item, dbname='BioGRID')
    card.swiss_model = get_dbreference(item, dbname='SMR')
    card.dip = get_dbreference(item, dbname='DIP')
    card.elm = get_dbreference(item, dbname='ELM')
    card.intact = get_dbreference(item, dbname='IntAct')
    card.mint = get_dbreference(item, dbname='MINT')
    card.bindingdb = get_dbreference(item, dbname='BindingDB')
    card.prodom = get_dbreference(item, dbname='ProDom')
    card.string = get_dbreference(item, dbname='STRIM')
    card.iptmnet = get_dbreference(item, dbname='iPTMnet')
    card.phosphositeplus = get_dbreference(item, dbname='PhosphoSitePlus')

    #card.pdbs = get_pdbs(item)

    return card
