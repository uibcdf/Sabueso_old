
form_name = 'uniprotkb_XMLDict'

def get_cards(molecular_system, indices='all'):

    from sabueso.cards.entity_cards import ProteinCard
    from sabueso.cards.stack_of_cards import StackOfCards
    from sabueso.tools.uniprotkb_XMLDict import get_name
    from sabueso.tools.uniprotkb_XMLDict import get_alternative_names
    from sabueso.tools.uniprotkb_XMLDict import get_organism_common_name
    from sabueso.tools.uniprotkb_XMLDict import get_organism_scientific_name
    from sabueso.tools.uniprotkb_XMLDict import get_uniprot
    from sabueso.tools.uniprotkb_XMLDict import get_dbreference
    from sabueso.tools.uniprotkb_XMLDict import get_pdbs
    from sabueso.tools.uniprotkb_XMLDict import get_host
    from sabueso.tools.uniprotkb_XMLDict import get_canonical_sequence

    stack = StackOfCards()

    card = ProteinCard()

    card.name = get_name(molecular_system)
    card.alternative_names = get_alternative_names(molecular_system)

    card.organism_common_name = get_organism_common_name(molecular_system)
    card.organism_scientific_name = get_organism_scientific_name(molecular_system)

    card.canonical_sequence = get_canonical_sequence(molecular_system)
    card.isoforms = []

    card.host =get_host(molecular_system)

    card.uniprot = get_uniprot(molecular_system)
    card.ec = get_dbreference(molecular_system, dbname='EC')
    card.chembl = get_dbreference(molecular_system, dbname='ChEMBL')
    card.biogrid = get_dbreference(molecular_system, dbname='BioGRID')
    card.swiss_model = get_dbreference(molecular_system, dbname='SMR')
    card.dip = get_dbreference(molecular_system, dbname='DIP')
    card.elm = get_dbreference(molecular_system, dbname='ELM')
    card.intact = get_dbreference(molecular_system, dbname='IntAct')
    card.mint = get_dbreference(molecular_system, dbname='MINT')
    card.bindingdb = get_dbreference(molecular_system, dbname='BindingDB')
    card.prodom = get_dbreference(molecular_system, dbname='ProDom')
    card.string = get_dbreference(molecular_system, dbname='STRIM')
    card.iptmnet = get_dbreference(molecular_system, dbname='iPTMnet')
    card.phosphositeplus = get_dbreference(molecular_system, dbname='PhosphoSitePlus')

    card.pdbs = get_pdbs(molecular_system)

    stack.add(card)

    return stack

