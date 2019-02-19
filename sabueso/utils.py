def load(json_file=None):

    import json

    with open(json_file, "r") as read_file:
        sabueso_json = json.load(read_file)

    if sabueso_json[0] == '"Protein"':
        from .protein import Protein as _Protein
        tmp_item = _Protein()
        tmp_item.card = json.loads(sabueso_json[1])
        del(_Protein)

    del(sabueso_json)
    return tmp_item

