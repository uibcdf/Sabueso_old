
def digest_string(item, form):

    if form=='string:uniprot_id':
        if not item.startswith('uniprot_id:'):
            item='uniprot_id:'+item

    return item

