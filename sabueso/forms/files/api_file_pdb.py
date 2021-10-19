form_name='file:pdb'

is_form = {
        'file:pdb': form_name
    }

def to_sabueso_PDBAtomicCoordinateEntry(filename):

    from .guess_format_version import guess_format_version
    from . import parsers

    version = guess_format_version(filename)

    output = None

    if version == '3.3':

        output = parsers.format33(filename)

    else:

        raise NotImplementedError

    return output

###### Get

def get_entity_index(item, indices='all'):

    raise NotImplementedError()

def get_entity_name(item, indices='all'):

    raise NotImplementedError()

def get_entity_id(item, indices='all'):

    raise NotImplementedError()

def get_entity_type(item, indices='all'):

    raise NotImplementedError()

def get_n_entities(item, indices='all'):

    raise NotImplementedError()

def is_ion(item, indices='all'):

    raise NotImplementedError()

def is_water(item, indices='all'):

    raise NotImplementedError()

def is_cosolute(item, indices='all'):

    raise NotImplementedError()

def is_small_molecule(item, indices='all'):

    raise NotImplementedError()

def is_lipid(item, indices='all'):

    raise NotImplementedError()

def is_peptide(item, indices='all'):

    raise NotImplementedError()

def is_protein(item, indices='all'):

    raise NotImplementedError()

def is_rna(item, indices='all'):

    raise NotImplementedError()

def is_dna(item, indices='all'):

    raise NotImplementedError()

