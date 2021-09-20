def to_PDBAtomicCoordinateEntry(filename):

    from .guess_format_version import guess_format_version
    from . import parsers

    version = guess_format_version(filename)

    output = None

    if version == '3.3':

        output = parsers.format33(filename)

    else:

        raise NotImplementedError

    return output

