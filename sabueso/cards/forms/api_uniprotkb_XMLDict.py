
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

    stack = StackOfCards()

    card = ProteinCard()

    card.name = get_name(molecular_system)
    card.alternative_names = get_alternative_names(molecular_system)

    card.organism_common_name = get_organism_common_name(molecular_system)
    card.organism_scientific_name = get_organism_scientific_name(molecular_system)

    card.host =get_host(molecular_system)

    card.uniprot = get_uniprot(molecular_system)
    card.ec = get_dbreference(molecular_system, dbname='EC')
    card.chembl = get_dbreference(molecular_system, dbname='ChEMBL')
    card.biogrid = get_dbreference(molecular_system, dbname='BioGRID')
    card.proteinmodelportal = get_dbreference(molecular_system, dbname='ProteinModelPortal')
    card.swiss_model = get_dbreference(molecular_system, dbname='SMR')
    card.dip = get_dip(molecular_system)
    card.elm = get_elm(molecular_system)
    card.intact = get_intact(molecular_system)
    card.mint = get_mint(molecular_system)
    card.bindingdb = get_bindingdb(molecular_system)
    card.prodom = get_prodom(molecular_system)
    card.string = get_string(molecular_system)
    card.iptmnet = get_iptmnet(molecular_system)
    card.phosphositeplus = get_phosphositeplus(molecular_system)

    card.pdbs = get_pdbs(molecular_system)


    stack.add(card)

    return stack

