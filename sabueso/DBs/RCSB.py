# There are already some opensource tools to extract information
# from the RCSB:
# https://github.com/williamgilpin/pypdb
# https://github.com/biopython/biopython


def card_pdb(pdb=None, card=None):

    if card is None:
        from sabueso.fields.pdb import _pdb_dict
        tmp_card = _deepcopy(_pdb_dict)
        del(_pdb_dict)
    else:
        tmp_card = _deepcopy(card)

    if uniprot is not None:
        tmp_card['UniProt'].append(uniprot)

    uniprot_id=tmp_card['UniProt'][0]

    url = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.xml'

    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/MolInterrogator || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)
    dict_result = dict_result['uniprot']['entry']

