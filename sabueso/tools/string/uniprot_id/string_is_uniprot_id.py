import re

## https://www.uniprot.org/help/accession_numbers

pattern= re.compile('[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}')

def string_is_uniprot_id(string):

    output = False

    if string.startswith('uniprot_id:'):
        output = True
    elif pattern.match(string):
        try:
            import requests
            request = requests.get('https://uniprot.org/uniprot/{}'.format(string), stream=True)
            if request.status_code == 200:
                output = True
        except:
            output = False

    return output

