
class Molecule():

    def __init__(self):

        self.id = None
        self.name = None
        self.chain_id = None
        self.fragment = None
        self.synonym = None
        self.enzyme_commision_number = None
        self.engineered = None
        self.mutation = None
        self.other_details = None

class Source():

    def __init__(self):

        self.molecule_id = None
        self.syntetic = None
        self.fragment = None
        self.organism_scientific = None
        self.organism_common = None
        self.organism_taxid = None
        self.strain = None
        self.variant = None
        self.cell_line = None
        self.atcc = None
        self.organ = None
        self.tissue = None
        self.cell = None
        self.organelle = None
        self.secretion = None
        self.cellular_location = None
        self.plasmid = None
        self.gene = None
        self.expression_system = None
        self.expression_system_common = None
        self.expression_system_taxid = None
        self.expression_system_strain = None
        self.expression_system_variant = None
        self.expression_system_cell_line = None
        self.expression_system_atcc_number = None
        self.expression_system_organ = None
        self.expression_system_tissue = None
        self.expression_system_cell = None
        self.expression_system_organelle = None
        self.expression_system_cellular_location = None
        self.expression_system_vector_type = None
        self.expression_system_vector = None
        self.expression_system_plasmid = None
        self.expression_system_gene = None
        self.other_details = None

class PDB():

    def __init__(self):

        self.version = None

        # Title section

        ## HEADER record
        self.deposition_date = None
        self.id = None
        self.classification = None

        ## OBSLTE record
        self.obsolete = False
        self.replacement_date = None
        self.replaced_with = []

        ## TITLE record
        self.title = []

        ## SPLIT record
        self.split = []

        ## CAVEAT record
        self.caveat = []

        ## COMPND record
        self.compounds = []

        ## SOURCE record
        self.sources = []

        ## KEYWDS record
        self.keywords = None

        ## EXPDTA record
        self.experimental_data = None

        ## NUMMDL record
        self.n_models = None

        ## MDLTYP record
        self.model_type = None

        ## AUTHOR record
        self.authors = None

        ## REVDAT record
        self.modifications = None

        self.superseded = None  # SPRSDE record
        self.cite = None  # JRNL record
        self.remarks = None  # REMARK record

        # Primary structure section

        self.database_ref = None # DBREF, DBREF1/DBREF2 records
        self.seqadv = None # SEQADV record
        self.seqres = None # SEQRES record
        self.modres = None # MODRES record

        # Heterogen section

        self.HET_groups = None # HET record
        self.HET_name = None # HETNAM record
        self.HET_synonyms = None # HETNAM record
        self.HET_formula = None # FORMUL record

        # Secondary structure section

        self.helix = None # HELIX record
        self.sheet = None # SHEET record

        # Connectivity annotation

        self.disulfide_bonds = None # SSBOND record
        self.links = None # LINK record
        self.cis_conformations = None # CISPEP record

        # Miscellaneous features

        self.sites = None # SITE record

        # Crystallographic and coordinate transformation section

        self.unit_cell = None # CRYST1 record
        self.transformation = None # ORIGXn, SCALEn and MTRIXn records

        # Coordinate section

        self.models = None # all records

        # Connectivity section

        self.bonds = None # CONECT record


    def _heal(self):

        pass

