from sabueso._private.exceptions import BadCallError

arguments = [

    'entity_index',
    'entity_name',
    'entity_id',
    'entity_type',

    'n_entities',

    'n_ions',
    'n_waters',
    'n_cosolutes',
    'n_small_molecules',
    'n_peptides',
    'n_proteins',
    'n_dnas',
    'n_rnas',
    'n_lipids',

    ]


argument_synonyms = {
    'index': 'entity_index',
    'name': 'entity_name',
    'id': 'entity_id',
    'type': 'entity_type',
    'indices': 'entity_index',
    'names': 'entity_name',
    'ids': 'entity_id',
    'types': 'entity_type',
    'n_entity': 'n_entities',
    'n_ion': 'n_ions',
    'n_water': 'n_waters',
    'n_cosolute': 'n_cosolutes',
    'n_small_molecule': 'n_small_molecules',
    'n_peptide': 'n_peptides',
    'n_protein': 'n_proteins',
    'n_dna': 'n_dnas',
    'n_rna': 'n_rnas',
    'n_lipid': 'n_lipids',
}


def digest_argument(argument):

    output_argument = argument.lower()
    if output_argument in argument_synonyms:
        output_argument = argument_synonyms[output_argument]
    if output_argument in arguments:
        return output_argument
    else:
        raise BadCallError()

