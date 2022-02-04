import requests
from sabueso._private_tools.exceptions import DatabaseNotAccessible

def is_accessible():

    r = requests.get('https://www.uniprot.org/uniprot/', stream=True, timeout=5)
    return r.status_code == requests.codes.ok

def _checking_database(check=True):

    if check:
        if not is_accessible():
            raise DatabaseNotAccessible('UniProtKB')

    pass

