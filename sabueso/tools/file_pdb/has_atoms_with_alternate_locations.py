def has_atoms_with_alternate_locations(filename):

    from .to_PDBAtomicCoordinateEntry import to_PDBAtomicCoordinateEntry

    item = to_PDBAtomicCoordinateEntry(filename)

    return item.has_atoms_with_alternate_locations()

