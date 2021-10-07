import requests

def to_string_fasta_text(item):

    from sabueso.tools.database_UniProtKB import is_accessible as UniProtKB_is_accessible

    if item.startswith('uniprot:'):
        item=item[8:]

    url = 'https://www.uniprot.org/uniprot/'+item+'.fasta'
    headers = {'user-agent': 'Python lib at https://github.com/uibcdf/sabueso || prada.gracia@gmail.com'}
    r = requests.get(url, headers=headers, timeout=5)
    if not r.status_code == requests.codes.ok:
        if UniProtKB_is_accessible():
            raise ValueError(f'{string} is not a uniprot id string')
        else:
            raise ValueError('UniProtKB is not accessible. Check your internet connection.')

    fasta_text = r.text

    return fasta_text

