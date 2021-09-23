import xmltodict
import urllib
import requests
from sabueso.tools.database.UniProtKB import is_accessible as UniProtKB_is_accessible


def to_uniprotkb_dict(string):

    url = 'http://www.uniprot.org/uniprot/'+string+'.xml'
    headers = {'user-agent': 'Python lib at https://github.com/uibcdf/sabueso || prada.gracia@gmail.com'}
    r = requests.get(url, headers=headers, timeout=5)
    if not r.status_code == requests.codes.ok:
        if UniProtKBEntry_is_accessible():
            raise ValueError('The input argument is not a uniprot id string')
        else:
            raise ValueError('UniProtKBEntry is not accessible. Check your internet connection.')

    dict_result = xmltodict.parse(r.text)

    return dict_result

