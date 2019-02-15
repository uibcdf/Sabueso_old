import urllib as _urllib
import xmltodict as _xmltodict


def initialize_protein(protein=None):

    uniprot_id=protein._uniprot

    url = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.xml'

    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/MolInterrogator || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)
    dict_result = dict_result['uniprot']['entry']

    # Name
    protein.card['Name'].append(dict_result['name'])

    # Full Name
    protein.card['Full Name'].append(dict_result['protein']['recommendedName']['fullName'])

    # Short Name
    if 'shortName' in dict_result['protein']['recommendedName'].keys():
        protein.card['Short Name'].append(dict_result['protein']['recommendedName']['shortName'])

    # Alternative Name
    if 'alternativeName' in dict_result['protein'].keys():
        if type(dict_result['protein']['alternativeName'])==list:
            for alternativeName in dict_result['protein']['alternativeName']:
                protein.card['Alternative Name'].append(alternativeName['fullName'])
        else:
            protein.card['Alternative Name'].append(dict_result['protein']['alternativeName']['fullName'])

    # Type
    protein.card['Type'].append('Protein')

    # Organism
    if 'organism' in dict_result.keys():
        if type(dict_result['organism']['name'])==list:
            for name in dict_result['organism']['name']:
                if name['@type']=='scientific':
                    protein.card['Organism'].append(name['#text'])
        else:
            protein.card['Organism'].append(dict_result['organism']['name']['#text'])

    # Host
    if 'organismHost' in dict_result.keys():
        protein.card['Host'].append(dict_result['organismHost']['name'][0]['#text'])

    # Function
    if type(dict_result['comment'])== list:
        for comment in dict_result['comment']:
            if comment['@type']=='function':
                if type(comment['text'])==list:
                    for function in comment['text']:
                            protein.card['Function'].append(function['#text'])
                else:
                    try:
                        protein.card['Function'].append(comment['text']['#text'])
                    except:
                        protein.card['Function'].append(comment['text'])
    else:
        if dict_result['comment']['@type']=='function':
            protein.card['Function'].append(dict_result['comment']['text'])

    # Uniprot
    protein.card['UniProt'].append(dict_result['accession'])

    # Sequence
    protein.card['Sequence'].append(dict_result['sequence']['#text'].replace('\n',''))

    # FASTA
    url_fasta = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.fasta'
    request_fasta = urllib.request.Request(url_fasta)
    request_fasta.add_header('User-Agent', 'Python at https://github.com/uibcdf/MolInterrogator || prada.gracia@gmail.com')
    response_fasta = urllib.request.urlopen(request_fasta)
    fasta_result = response_fasta.read().decode('utf-8')
    protein.card['FASTA'].append(fasta_result)

    for dbreference in dict_result['dbReference']:

    # ChEMBL
        if dbreference['@type']=='ChEMBL':
            protein.card['ChEMBL'].append(dbreference['@id'])

    # BioGRID
        elif dbreference['@type']=='BioGRID':
            protein.card['BioGRID'].append(dbreference['@id'])

    # Protein Model Portal
        elif dbreference['@type']=='ProteinModelPortal':
            protein.card['ProteinModelPortal'].append(dbreference['@id'])

    # Swiss Model
        elif dbreference['@type']=='SMR':
            protein.card['Swiss-Model'].append(dbreference['@id'])

    # DIP
        elif dbreference['@type']=='DIP':
            protein.card['DIP'].append(dbreference['@id'])

    # ELM
        elif dbreference['@type']=='ELM':
            protein.card['ELM'].append(dbreference['@id'])

    # IntAct
        elif dbreference['@type']=='IntAct':
            protein.card['IntAct'].append(dbreference['@id'])

    # MINT
        elif dbreference['@type']=='MINT':
            protein.card['MINT'].append(dbreference['@id'])

    # BindingDB
        elif dbreference['@type']=='BindingDB':
            protein.card['BindingDB'].append(dbreference['@id'])

    # InterPro
        elif dbreference['@type']=='InterPro':
            protein.card['InterPro'].append(uniprot_id)

    # Pfam
        elif dbreference['@type']=='Pfam':
            protein.card['Pfam'].append(dbreference['@id'])

    # ProDom
        elif dbreference['@type']=='ProDom':
            protein.card['ProDom'].append(dbreference['@id'])

    # SUPFAM
        elif dbreference['@type']=='SUPFAM':
            protein.card['SUPFAM'].append(dbreference['@id'])

    # PDBs
        elif dbreference['@type']=='PDB':
            protein.card['PDB'].append(dbreference['@id'])

    del(url, request, response, xml_result, dict_result)
    del(url_fasta, request_fasta, response_fasta, fasta_result)

