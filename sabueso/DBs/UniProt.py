import urllib as _urllib
import xmltodict as _xmltodict

def _get_organism_scientific(uniprot=None):

    url = 'http://www.uniprot.org/uniprot/'+uniprot+'.xml'
    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/MolInterrogator || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)
    dict_result = dict_result['uniprot']['entry']
    tmp_name = None

    if 'organism' in dict_result.keys():
        if type(dict_result['organism']['name'])==list:
            for name in dict_result['organism']['name']:
                if name['@type']=='scientific':
                    tmp_name=name['#text']

    del(url,request,response,xml_result,dict_result)
    return tmp_name


def card_protein(uniprot=None, card=None, with_interactions=True):
    if card is None:
        from sabueso.fields.protein import _protein_dict
        tmp_card = _protein_dict.copy()
        tmp_card['UniProt'].append(uniprot)
        del(_protein_dict)
    else:
        tmp_card = card.copy()

    uniprot_id=tmp_card['UniProt'][0]

    url = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.xml'

    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/MolInterrogator || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)
    dict_result = dict_result['uniprot']['entry']

    # Name
    tmp_card['Name'].append(dict_result['name'])

    # Full Name
    tmp_card['Full Name'].append(dict_result['protein']['recommendedName']['fullName'])

    # Short Name
    if 'shortName' in dict_result['protein']['recommendedName'].keys():
        if type(dict_result['protein']['recommendedName']['shortName'])==list:
            for shortName in dict_result['protein']['recommendedName']['shortName']:
                tmp_card['Short Name'].append(shortName)
        else:
            tmp_card['Short Name'].append(dict_result['protein']['recommendedName']['shortName'])

    # Alternative Name
    if 'alternativeName' in dict_result['protein'].keys():
        if type(dict_result['protein']['alternativeName'])==list:
            for alternativeName in dict_result['protein']['alternativeName']:
                tmp_card['Alternative Name'].append(alternativeName['fullName'])
        else:
            tmp_card['Alternative Name'].append(dict_result['protein']['alternativeName']['fullName'])

    # Type
    tmp_card['Type'].append('Protein')

    # Organism
    if 'organism' in dict_result.keys():
        if type(dict_result['organism']['name'])==list:
            for name in dict_result['organism']['name']:
                if name['@type']=='scientific':
                    tmp_card['Organism Scientific'].append(name['#text'])
                if name['@type']=='common':
                    tmp_card['Organism'].append(name['#text'])
        else:
            tmp_card['Organism'].append(dict_result['organism']['name']['#text'])

    # Host
    if 'organismHost' in dict_result.keys():
        tmp_card['Host'].append(dict_result['organismHost']['name'][0]['#text'])

    # Function
    # Subunit Structure
    # Interactions
    if type(dict_result['comment'])== list:
        for comment in dict_result['comment']:

            if comment['@type']=='function':
                if type(comment['text'])==list:
                    for function in comment['text']:
                            tmp_card['Function'].append(function['#text'])
                else:
                    try:
                        tmp_card['Function'].append(comment['text']['#text'])
                    except:
                        tmp_card['Function'].append(comment['text'])

            if comment['@type']=='subunit':
                if type(comment['text'])==list:
                    for function in comment['text']:
                            tmp_card['Subunit Structure'].append(function['#text'])
                else:
                    try:
                        tmp_card['Subunit Structure'].append(comment['text']['#text'])
                    except:
                        tmp_card['Subunit Structure'].append(comment['text'])

            if with_interactions:
                if comment['@type']=='interaction':
                    from sabueso.fields.interaction import _interaction_dict
                    tmp_interaction = _interaction_dict.copy()
                    tmp_interactant=tmp_interaction['Interactants'][0]
                    tmp_interactant['UniProt']=uniprot_id
                    tmp_interactant['IntAct']=comment['interactant'][0]['@intactId']
                    tmp_interactant['Organism Scientific']=tmp_card['Organism Scientific'][0]
                    tmp_interactant['Short Name']=tmp_card['Short Name']
                    tmp_interactant=tmp_interaction['Interactants'][1]
                    tmp_interactant['UniProt']=comment['interactant'][1]['id']
                    tmp_interactant['IntAct']=comment['interactant'][1]['@intactId']
                    tmp_interactant['Short Name']=comment['interactant'][1]['label']
                    if comment['organismsDiffer']=='false':
                        tmp_interactant['Organism']=tmp_card['Organism Scientific'][0]
                    else:
                        tmp_uniprot = comment['interactant'][1]['id']
                        tmp_organism = _get_organism_scientific(tmp_uniprot)
                        tmp_interactant['Organism Scientific']=tmp_organism
                        del(tmp_uniprot,tmp_organism)
                    tmp_card['Interactions'].append(tmp_interaction)
                    del(tmp_interaction,tmp_interactant,_interaction_dict)
    else:
        if dict_result['comment']['@type']=='function':
            tmp_card['Function'].append(dict_result['comment']['text'])
        if dict_result['comment']['@type']=='subunit':
            tmp_card['Subunit Structure'].append(dict_result['comment']['text'])

    # Uniprot

    if type(dict_result['accession'])== list:
        for ii in dict_result['accession']:
            tmp_card['UniProt'].append(ii)
    else:
        tmp_card['UniProt'].append(dict_result['accession'])

    # Sequence
    tmp_card['Sequence'].append(dict_result['sequence']['#text'].replace('\n',''))

    # FASTA
    url_fasta = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.fasta'
    request_fasta = _urllib.request.Request(url_fasta)
    request_fasta.add_header('User-Agent', 'Python at https://github.com/uibcdf/MolInterrogator || prada.gracia@gmail.com')
    response_fasta = _urllib.request.urlopen(request_fasta)
    fasta_result = response_fasta.read().decode('utf-8')
    tmp_card['FASTA'].append(fasta_result)

    for dbreference in dict_result['dbReference']:

    # ChEMBL
        if dbreference['@type']=='ChEMBL':
            tmp_card['ChEMBL'].append(dbreference['@id'])

    # BioGRID
        elif dbreference['@type']=='BioGRID':
            tmp_card['BioGRID'].append(dbreference['@id'])

    # Protein Model Portal
        elif dbreference['@type']=='ProteinModelPortal':
            tmp_card['ProteinModelPortal'].append(dbreference['@id'])

    # Swiss Model
        elif dbreference['@type']=='SMR':
            tmp_card['Swiss-Model'].append(dbreference['@id'])

    # DIP
        elif dbreference['@type']=='DIP':
            tmp_card['DIP'].append(dbreference['@id'])

    # ELM
        elif dbreference['@type']=='ELM':
            tmp_card['ELM'].append(dbreference['@id'])

    # IntAct
        elif dbreference['@type']=='IntAct':
            tmp_card['IntAct'].append(dbreference['@id'])

    # MINT
        elif dbreference['@type']=='MINT':
            tmp_card['MINT'].append(dbreference['@id'])

    # BindingDB
        elif dbreference['@type']=='BindingDB':
            tmp_card['BindingDB'].append(dbreference['@id'])

    # InterPro
        elif dbreference['@type']=='InterPro':
            tmp_card['InterPro'].append(uniprot_id)

    # Pfam
        elif dbreference['@type']=='Pfam':
            tmp_card['Pfam'].append(dbreference['@id'])

    # ProDom
        elif dbreference['@type']=='ProDom':
            tmp_card['ProDom'].append(dbreference['@id'])

    # SUPFAM
        elif dbreference['@type']=='SUPFAM':
            tmp_card['SUPFAM'].append(dbreference['@id'])

    # PDBs
        elif dbreference['@type']=='PDB':
            tmp_card['PDB'].append(dbreference['@id'])

    del(url, request, response, xml_result, dict_result)
    del(url_fasta, request_fasta, response_fasta, fasta_result)

    return tmp_card
