
class TitleSection():

    def __init__(self):

        self.header = None
        self.obslte = None
        self.title = None
        self.split = None
        self.caveat = None
        self.compnd = None
        self.source = None
        self.keywds = None
        self.expdta = None
        self.nummdl = None
        self.mdltyp = None
        self.author = None
        self.revdat = None
        self.sprsde = None
        self.jrnl = None
        self.remarks = None


class PrimaryStructureSection():

    def __init__(self):

        self.dbref = None
        self.dbref1_dbref2 = None
        self.seqadv = None
        self.seqres = None
        self.modres = None


class HeterogenSection():

    def __init__(self):

        self.het = None
        self.hetnam = None
        self.hetsyn = None
        self.formul = None


class SecondaryStructureSection():

    def __init__(self):

        self.helix = None
        self.sheet = None


class ConnectivityAnnotationSection():

    def __init__(self):

        self.ssbond = None
        self.link = None
        self.cispep = None

class MiscellaneousFeaturesSection():

    def __init__(self):

        self.site = None


class CrystallographicAndCoordinateTransformationSection():

    def __init__(self):

        self.cryst1 = None
        self.origxn = None
        self.scalen = None
        self.mtrixn = None


class CoordinateSection():

    def __init__(self):

        self.model = None
        self.atom = None
        self.anisou = None
        self.ter = None
        self.hetatm = None
        self.endmdl = None


class ConnectivitySection():

    def __init__(self):

        self.conect = None


class BookkeepingSection():

    def __init__(self):

        self.master = None
        self.end = None


class HeaderRecord():

    def __init__(self):

        self.classification = None
        self.depDate = None
        self.idCode = None


class ObslteRecord():

    def __init__(self):

        self.classification = None
        self.depDate = None
        self.idCode = None
        self.rIdCode = None


class TitleRecord():

    def __init__(self):

        self.title = None


class SplitRecord():

    def __init__(self):

        self.idCode = None


class CaveatRecord():

    def __init__(self):

        self.idCode = None
        self.comment = None


class CompndRecord():

    def __init__(self):

        self.mol_id = None
        self.molecule = None
        self.chain = None
        self.fragment = None
        self.synonym = None
        self.ec = None
        self.engineered = None
        self.mutation = None
        self.other_details = None

class SourceRecord():

    def __init__(self):

        self.mol_id = None
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


class KeywdsRecord():

        self.keywds = None


class ExpdtaRecord():

        self.technique = None


class NummdlRecord():

        self.modelNumber = None


class MdltypRecord():

        self.comment = None


class AuthorRecord():

        self.authorList = None


class RevdatRecord():

        self.modNum = None
        self.modDate = None
        self.modId = None
        self.modType = None
        self.record = None


class SprsdeRecord():

        self.sprsdeDate = None
        self.idCode = None
        self.sIdCode = None


class JrnlRecord():

    def __init__(self):

        self.auth = None
        self.titl = None
        self.edit = None
        self.ref = None
        self.publ = None
        self.refn = None
        self.pmid = None
        self.doi = None

class RemarkRecord():

    def __init__(self):

        self.id = None
        self.message = None


class DbrefRecord():

    def __init__(self):

        self.idCode = None
        self.chainId = None
        self.seqBegin = None
        self.insertBegin = None
        self.seqEnd = None
        self.insertEnd = None
        self.database = None
        self.dbAccession = None
        self.dbIdCode = None
        self.dbseqBegin = None
        self.idinsBeg = None
        self.dbseqEnd = None
        self.dbinsEnd = None


class Dbref1Dbref2Record():

    def __init__(self):

        self.idCode = None
        self.chainId = None
        self.seqBegin = None
        self.insertBegin = None
        self.seqEnd = None
        self.insertEnd = None
        self.database = None
        self.dbAccession = None
        self.dbIdCode = None
        self.dbseqBegin = None
        self.dbseqEnd = None


class SeqadvRecord():

    def __init__(self):

        self.idCode = None
        self.resName = None
        self.chainId = None
        self.seqNum = None
        self.iCode = None
        self.database = None
        self.dbAccession = None
        self.dbRes = None
        self.dbSeq = None
        self.conflict = None


class SeqresRecord():

    def __init__(self):

        self.chainId = None
        self.numRes = None
        self.resName = []


class ModresRecord():

    def __init__(self):

        self.idCode = None
        self.resName = None
        self.chainId = None
        self.seqNum = None
        self.iCode = None
        self.stdRes = None
        self.comment = None


class HetRecord():

    def __init__(self):

        self.hetId = None
        self.chainId = None
        self.seqNum = None
        self.iCode = None
        self.numHetAtoms = None
        self.text = None


class HetnamRecord():

    def __init__(self):

        self.hetId = None
        self.text = None


class HetsynRecord():

    def __init__(self):

        self.hetId = None
        self.hetSynonyms = []


class FormulRecord():

    def __init__(self):

        self.compNum = None
        self.hetId = None
        self.asterisk = False
        self.text = ''




class PDBFile33():

    def __init__(self):

        self.version = '3.3'

        self.title = TitleSection()
        self.primary_structure = PrimaryStructureSection()
        self.heterogen = HeterogenSection()
        self.secondary_structure = SecondaryStructureSection()
        self.connectivity_annotation = ConnectivityAnnotationSection()
        self.miscellaneour_features = MiscellaneousFeaturesSection()
        self.crystallographic_and_coordinate_transformation = CrystallographicAndCoordinateTransformationSection()
        self.coordinate = CoordinateSection()
        self.connectivity = ConnectivitySection()
        self.bookkeeping = BookkeepingSection()

    def _heal(self):

        pass

