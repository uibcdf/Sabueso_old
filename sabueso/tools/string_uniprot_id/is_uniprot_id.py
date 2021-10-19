import re

## https://www.uniprot.org/help/accession_numbers

pattern= re.compile('[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}')

def is_uniprot_id(item):

    output = False

    if type(item)==str:

        if item.startswith('uniprot_id:'):
            output = True
        elif pattern.match(item):
            try:
                import requests
                request = requests.get('https://uniprot.org/uniprot/{}'.format(item), stream=True)
                if request.status_code == 200:
                    output = True
            except:
                output = False

    return output

