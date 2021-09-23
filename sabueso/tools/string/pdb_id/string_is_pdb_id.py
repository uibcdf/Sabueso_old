import re

pattern= re.compile('[0-9][a-zA-Z_0-9]{3}')


def string_is_pdb_id(string):

    output = False

    if pattern.match(string):
        try:
            import requests
            request = requests.get('https://files.rcsb.org/download/{}.pdb'.format(string), stream=True)
            if request.status_code == 200:
                output = True
        except:
            output = False

    return output

