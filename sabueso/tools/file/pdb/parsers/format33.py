#https://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html

dict_database_name = {
        'GB' : 'GenBank',
        'PDB' : 'Protein Data Bank',
        'UNP' : 'UNIPROT',
        'NORINE' : 'Norine',
        'UNIMES' : 'UNIMES',
        }

def format33(filename):

    from sabueso.native.pdbfile import PDBFile33
    from sabueso.native.pdbfile import HeaderRecord, ObslteRecord, TitleRecord, SplitRecord,
    CaveatRecord, CompndRecord, SourceRecord, KeywdsRecord, ExpdtaRecord, NummdlRecord,
    MdltypRecord, AuthorRecord, RevdatRecord, SprsdeRecord, JrnlRecord, RemarkRecord, DbrefRecord,
    Dbref1Dbref2Record, SeqadvRecord, SeqresRecord, ModresRecord, HetRecord, HetnamRecord,
    HetsynRecord, FormulRecord
    from sabueso.tools.file.pdb import download

    pdb = PDBFile33()

    #if not is_filename(item):
    #    raise ValueError

    with open(filename, 'r') as fff:
        lines = fff.readlines()

    n_lines = len(lines)
    counter = 0

    while counter<n_lines:

        line = lines[counter]
        record = line[0:6]

        #print(counter, n_lines, record)

        ### HEADER
        if record=='HEADER':

            if pdb.id is not None:
                raise ValueError('There are multiple HEADER lines... the parser works with only one.')

            pdb.classification = line[10:50].strip()
            pdb.deposition_date = line[50:59]
            pdb.id = line[62:66]

            counter += 1

        ### OBSLTE
        elif record=='OBSLTE':

            if pdb.replacement_date is not None:
                raise ValueError('There are multiple OBSLTE lines... the parser works with only one.')

            pdb.obsolete = True
            pdb.replacement_date = line[11:20]
            pdb.replaced_with = []
            position=31
            while not line[position:position+4].isspace():
                pdb.replace_with.append(line[position:position+4])
                position+=5
                if position==81:
                    break

            counter += 1

        ### TITLE
        elif record=='TITLE ':

            while record=='TITLE ':

                if line[8:10]=='  ':
                    pdb.title.append(line[10:80].rstrip())
                else:
                    pdb.title[-1]+=line[10:80].rstrip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### SPLIT
        elif record=='SPLIT ':

            while record=='SPLIT ':

                position=11
                while not line[position:position+4].isspace():
                    pdb.split.append(line[position:position+4])
                    position+=5
                    if position==81:
                        break

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### CAVEAT
        elif record=='CAVEAT':

            while record=='CAVEAT':

                if line[8:10]=='  ':
                    pdb.caveat.append(line[10:80].rstrip())
                else:
                    pdb.caveat[-1]+=line[10:80].rstrip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### COMPND
        elif record=='COMPND':

            while record=='COMPND':

                aux = line[10:80].strip()
                if aux.startswith('MOL_ID:'): ### MOL_ID
                    molecule = Molecule()
                    pdb.compounds.append(molecule)
                    aux = aux.replace('MOL_ID:', '').replace(';', '')
                    molecule.id = [int(ii) for ii in aux.split(',')]
                elif aux.startswith('MOLECULE:'): ### MOLECULE
                    aux = aux.replace('MOLECULE:', '')
                    molecule.name = [ii.strip() for ii in aux.split(';')]
                elif aux.startswith('CHAIN:'): ### CHAIN
                    aux = aux.replace('CHAIN:', '').replace(';', '')
                    molecule.chain_id = [ii.strip() for ii in aux.split(',')]
                elif aux.startswith('FRAGMENT:'): ### FRAGMENT
                    aux = aux.replace('FRAGMENT:', '')
                    molecule.fragment = [ii.strip() for ii in aux.split(';')]
                elif aux.startswith('EC:'): ### EC
                    aux = aux.replace('EC:', '')
                    molecule.enzyme_commision_number = [ii.strip() for ii in aux.split(';')]
                elif aux.startswith('SYNONYM:'): ### SYNONYM
                    aux = aux.replace('SYNONYM:', '').replace(';', '')
                    molecule.synonym = [ii.strip() for ii in aux.split(',')]
                elif aux.startswith('ENGINEERED:'): ### ENGINEERED
                    aux = aux.replace('ENGINEERED:', '')
                    molecule.engineered = aux.strip()
                elif aux.startswith('MUTATION:'): ### MUTATION
                    aux = aux.replace('MUTATION:', '')
                    molecule.mutation = aux.strip()
                elif aux.startswith('OTHER_DETAILS:'): ### OTHER DETAILS
                    aux = aux.replace('OTHER_DETAILS:', '').replace(';', '')
                    molecule.other_details = aux.strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### SOURCE
        elif record=='SOURCE':

            while record=='SOURCE':

                aux = line[10:80].strip()
                if aux.startswith('MOL_ID:'): ### MOL_ID
                    source = Source()
                    pdb.sources.append(source)
                    aux = aux.replace('MOL_ID:', '').replace(';', '')
                    source.molecule_id = [int(ii) for ii in aux.split(',')]
                elif aux.startswith('SYNTHETIC:'): ### SYNTHETIC
                    aux = aux.replace('SYNTHETIC:', '').replace(';', '')
                    source.synthetic = aux.strip()
                elif aux.startswith('FRAGMENT:'): ### FRAGMENT
                    aux = aux.replace('FRAGMENT:', '').replace(';', '')
                    source.fragment = aux.strip()
                elif aux.startswith('ORGANISM_SCIENTIFIC:'): ### ORGANISM_SCIENTIFIC
                    aux = aux.replace('ORGANISM_SCIENTIFIC:', '').replace(';', '')
                    source.organism_scientific = aux.strip()
                elif aux.startswith('ORGANISM_COMMON:'): ### ORGANISM_COMMON
                    aux = aux.replace('ORGANISM_COMMON:', '').replace(';', '')
                    source.organism_common = aux.strip()
                elif aux.startswith('ORGANISM_TAXID:'): ### ORGANISM_TAXID
                    aux = aux.replace('ORGANISM_TAXID:', '').replace(';', '')
                    source.organism_taxid = aux.strip()
                elif aux.startswith('STRAIN:'): ### STRAIN
                    aux = aux.replace('STRAIN:', '').replace(';', '')
                    source.strain = aux.strip()
                elif aux.startswith('VARIANT:'): ### VARIANT
                    aux = aux.replace('VARIANT:', '').replace(';', '')
                    source.variant = aux.strip()
                elif aux.startswith('CELL_LINE:'): ### CELL_LINE
                    aux = aux.replace('CELL_LINE:', '').replace(';', '')
                    source.cell_line = aux.strip()
                elif aux.startswith('ATCC:'): ### ATCC
                    aux = aux.replace('ATCC:', '').replace(';', '')
                    source.atcc = aux.strip()
                elif aux.startswith('ORGAN:'): ### ORGAN
                    aux = aux.replace('ORGAN:', '').replace(';', '')
                    source.organ = aux.strip()
                elif aux.startswith('TISSUE:'): ### TISSUE
                    aux = aux.replace('TISSUE:', '').replace(';', '')
                    source.tissue = aux.strip()
                elif aux.startswith('CELL:'): ### CELL
                    aux = aux.replace('CELL:', '').replace(';', '')
                    source.cell = aux.strip()
                elif aux.startswith('ORGANELLE:'): ### ORGANELLE
                    aux = aux.replace('ORGANELLE:', '').replace(';', '')
                    source.organelle = aux.strip()
                elif aux.startswith('SECRETION:'): ### SECRETION
                    aux = aux.replace('SECRETION:', '').replace(';', '')
                    source.secretion = aux.strip()
                elif aux.startswith('CELLULAR_LOCATION:'): ### CELLULAR_LOCATION
                    aux = aux.replace('CELLULAR_LOCATION:', '').replace(';', '')
                    source.cellular_location = aux.strip()
                elif aux.startswith('PLASMID:'): ### PLASMID
                    aux = aux.replace('PLASMID:', '').replace(';', '')
                    source.plasmid = aux.strip()
                elif aux.startswith('GENE:'): ### GENE
                    aux = aux.replace('GENE:', '').replace(';', '')
                    source.gene = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM:'): ### EXPRESSION_SYSTEM
                    aux = aux.replace('EXPRESSION_SYSTEM:', '').replace(';', '')
                    source.expression_system = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_COMMON:'): ### EXPRESSION_SYSTEM_COMMON
                    aux = aux.replace('EXPRESSION_SYSTEM_COMMON:', '').replace(';', '')
                    source.expression_system_common = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_TAXID:'): ### EXPRESSION_SYSTEM_TAXID
                    aux = aux.replace('EXPRESSION_SYSTEM_TAXID:', '').replace(';', '')
                    source.expression_system_taxid = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_STRAIN:'): ### EXPRESSION_SYSTEM_STRAIN
                    aux = aux.replace('EXPRESSION_SYSTEM_STRAIN:', '').replace(';', '')
                    source.expression_system_strain = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_VARIANT:'): ### EXPRESSION_SYSTEM_VARIANT
                    aux = aux.replace('EXPRESSION_SYSTEM_VARIANT:', '').replace(';', '')
                    source.expression_system_variant = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_CELL_LINE:'): ### EXPRESSION_SYSTEM_CELL_LINE
                    aux = aux.replace('EXPRESSION_SYSTEM_CELL_LINE:', '').replace(';', '')
                    source.expression_system_cell_line = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_ATCC_NUMBER:'): ### EXPRESSION_SYSTEM_ATCC_NUMBER
                    aux = aux.replace('EXPRESSION_SYSTEM_ATCC_NUMBER:', '').replace(';', '')
                    source.expression_system_atcc_number = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_ORGAN:'): ### EXPRESSION_SYSTEM_ORGAN
                    aux = aux.replace('EXPRESSION_SYSTEM_ORGAN:', '').replace(';', '')
                    source.expression_system_organ = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_TISSUE:'): ### EXPRESSION_SYSTEM_TISSUE
                    aux = aux.replace('EXPRESSION_SYSTEM_TISSUE:', '').replace(';', '')
                    source.expression_system_tissue = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_CELL:'): ### EXPRESSION_SYSTEM_CELL
                    aux = aux.replace('EXPRESSION_SYSTEM_CELL:', '').replace(';', '')
                    source.expression_system_cell = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_ORGANELLE:'): ### EXPRESSION_SYSTEM_ORGANELLE
                    aux = aux.replace('EXPRESSION_SYSTEM_ORGANELLE:', '').replace(';', '')
                    source.expression_system_organelle = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_CELLULAR_LOCATION:'): ### EXPRESSION_SYSTEM_CELLULAR_LOCATION
                    aux = aux.replace('EXPRESSION_SYSTEM_CELLULAR_LOCATION:', '').replace(';', '')
                    source.expression_system_cellular_location = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_VECTOR_TYPE:'): ### EXPRESSION_SYSTEM_VECTOR_TYPE
                    aux = aux.replace('EXPRESSION_SYSTEM_VECTOR_TYPE:', '').replace(';', '')
                    source.expression_system_vector_type = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_VECTOR:'): ### EXPRESSION_SYSTEM_VECTOR
                    aux = aux.replace('EXPRESSION_SYSTEM_VECTOR:', '').replace(';', '')
                    source.expression_system_vector = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_PLASMID:'): ### EXPRESSION_SYSTEM_PLASMID
                    aux = aux.replace('EXPRESSION_SYSTEM_PLASMID:', '').replace(';', '')
                    source.expression_system_plasmid = aux.strip()
                elif aux.startswith('EXPRESSION_SYSTEM_GENE:'): ### EXPRESSION_SYSTEM_GENE
                    aux = aux.replace('EXPRESSION_SYSTEM_GENE:', '').replace(';', '')
                    source.expression_system_gene = aux.strip()
                elif aux.startswith('OTHER_DETAILS:'): ### OTHER DETAILS
                    aux = aux.replace('OTHER_DETAILS:', '').replace(';', '')
                    source.other_details = aux.strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### KEYWDS
        elif record=='KEYWDS':

            while record=='KEYWDS':

                if line[8:10]=='  ':
                    pdb.keywords = []
                    aux = [ii.strip() for ii in line[10:80].split(',')]
                    pdb.keywords += aux
                else:
                    aux = [ii.strip() for ii in line[10:80].split(',')]
                    pdb.keywords += aux

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### EXPDTA
        elif record=='EXPDTA':

            while record=='EXPDTA':

                if line[8:10]=='  ':
                    pdb.experimental_data = ''
                    pdb.experimental_data += line[10:80].strip()
                else:
                    pdb.experimental_data += line[10:80].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### NUMMDL
        elif record=='NUMMDL':

            pdb.n_models = int(line[10:14])
            counter += 1

        ### MDLTYP
        elif record=='MDLTYP':

            while record=='MDLTYP':

                if line[8:10]=='  ':
                    pdb.model_type = ''
                    pdb.model_type += line[10:80].strip()
                else:
                    pdb.model_type += line[10:80].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### AUTHOR
        elif record=='AUTHOR':

            while record=='AUTHOR':

                if line[8:10]=='  ':
                    pdb.authors = ''
                    pdb.authors += line[10:80].strip()
                else:
                    pdb.authors += line[10:80].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### REVDAT
        elif record=='REVDAT':

            while record=='REVDAT':

                if line[10:12]=='  ':
                    modification = Modification()
                    pdb.modifications.append(modification)
                    modification.id = int(line[7:10])
                    modification.date = line[13:22]
                    modification.type = int(line[31])
                    position=39
                    while not line[position:position+6].isspace():
                        modification.changes.append(line[position:position+6].strip())
                        position+=8
                        if position>=66:
                            break
                else:
                    position=39
                    while not line[position:position+6].isspace():
                        modification.changes.append(line[position:position+6].strip())
                        position+=8
                        if position>=66:
                            break

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### SPRSDE
        elif record=='SPRSDE':

            while record=='SPRSDE':

                if line[8:10]=='  ':
                    superseded = Superseded()
                    pdb.superseded.append(superseded)
                    modification.date = line[11:20]
                    position=31
                    while not line[position:position+4].isspace():
                        modification.changes.append(line[position:position+4].strip())
                        position+=6
                        if position>=75:
                            break
                else:
                    while not line[position:position+4].isspace():
                        modification.changes.append(line[position:position+4].strip())
                        position+=6
                        if position>=75:
                            break

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### JRNL
        elif record=='JRNL  ':

            pdb.cite=Cite()

            while record=='JRNL  ':

                aux = line[12:16]
                if aux == 'AUTH': ### AUTH
                    if line[16:18]=='  ':
                        pdb.cite.authors=line[19:79].strip()
                    else:
                        pdb.cite.authors+=line[19:79].strip()
                elif aux.startswith('TITL'): ### TITL
                    if line[16:18]=='  ':
                        pdb.cite.title=line[19:79].strip()
                    else:
                        pdb.cite.title+=line[19:79].strip()
                elif aux.startswith('EDIT'): ### EDIT
                    if line[16:18]=='  ':
                        pdb.cite.editors=line[19:79].strip()
                    else:
                        pdb.cite.editors+=line[19:79].strip()
                elif aux.startswith('REF '): ### REF
                    if line[16:18]=='  ':
                        pdb.cite.reference=line[19:79].strip()
                    else:
                        pdb.cite.reference+=line[19:79].strip()
                elif aux.startswith('PUBL'): ### REF
                    if line[16:18]=='  ':
                        pdb.cite.publisher=line[19:79].strip()
                    else:
                        pdb.cite.publisher+=line[19:79].strip()
                elif aux.startswith('REFN'): ### REFN
                    if line[35:39] == 'ISSN':
                        pdb.cite.issn = line[40:65].strip()
                    elif line[35:39] == 'ESSN':
                        pdb.cite.essn = line[40:65].strip()
                elif aux.startswith('PMID'): ### PMID
                    pdb.cite.pmid = line[19:79].strip()
                elif aux.startswith('DOI '): ### DOI
                    pdb.cite.doi = line[19:79].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### REMARKS
        elif record=='REMARK':

            mark_id = -1

            while record=='REMARK':

                if line[11:79].isspace() and int(line[7:10])!=mark_id:
                    remark = Remark()
                    pdb.remarks.append(remark)
                    remark.id = int(line[7:10])
                    remark.message = ''
                    mark_id = int(line[7:10])
                else:
                    remark.message += line[11:79].strip()+'\n'

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### DBREF
        elif record=='DBREF ':

            while record=='DBREF ':

                db_ref=Database_ref()
                pdb.database_refs.append(db_ref)

                db_ref.chain_id = line[12]
                db_ref.seq_begin = int(line[14:18])
                db_ref.insert_begin = line[18]
                db_ref.seq_end = int(line[20:24])
                db_ref.insert_end = line[24]
                db_ref.database = dict_database_name[line[26:32].strip()]
                db_ref.database_accesion_code = line[33:41].strip()
                db_ref.database_id_code = line[42:54].strip()
                db_ref.seq_begin_in_database = int(line[55:60])
                db_ref.insert_begin_in_database = line[60]
                db_ref.seq_end_in_database = int(line[62:67])
                db_ref.insert_end_in_database = line[67]

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### DBREF1/DBREF2
        elif record=='DBREF1':

            db_ref=Database_ref()
            pdb.database_refs.append(db_ref)

            db_ref.chain_id = line[12]
            db_ref.seq_begin = int(line[14:18])
            db_ref.insert_begin = line[18]
            db_ref.seq_end = int(line[20:24])
            db_ref.insert_end = line[24]
            db_ref.database = dict_database_name[line[26:32].strip()]
            db_ref.database_id_code = line[47:67].strip()

            counter += 1
            line = lines[counter]
            record = line[0:6]

            if record!='DBREF2':
                raise ValueError('DBREF1 is not followed by DBREF2')

            if db_ref.chain_id != line[12]:
                raise ValueError('DBREF2 with different chain id')

            db_ref.database_accesion_code = line[18:40].strip()
            db_ref.seq_begin_in_database = int(line[45:55])
            db_ref.seq_end_in_database = int(line[57:67])

            counter += 1
            line = lines[counter]
            record = line[0:6]

        ### SEQADV
        elif record=='SEQADV':

            while record=='SEQADV':

                seqadv=Seqadv()
                pdb.seqadv.append(seqadv)

                seqadv.pdbid = line[7:11]
                seqadv.residue_name = line[12:15]
                seqadv.chain_id = line[16]
                seqadv.sequence_number = int(line[18:22])
                seqadv.insertion_code = line[22]
                seqadv.database = dict_database_name[line[24:28].strip()]
                seqadv.database_accesion_code = line[29:38].strip()
                seqadv.database_residue_name = line[39:42].strip()
                seqadv.database_sequence_number = int(line[43:48])
                seqadv.conflict = line[49:70].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### SEQRES
        elif record=='SEQRES':

            while record=='SEQRES':

                if int(line[7:10])==1:
                    seqres=Seqres()
                    pdb.seqres.append(seqres)
                    seqres.chain_id = line[11]
                    seqres.n_residues = int(line[13:17])

                position=19
                while not line[position:position+3].isspace():
                    seqres.residue_names.append(line[position:position+3].strip())
                    position+=4
                    if position>=70:
                        break

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### MODRES
        elif record=='MODRES':

            while record=='MODRES':

                modres=Modres()
                pdb.modres.append(modres)

                modres.pdbid = line[7:11]
                modres.residue_name = line[12:15]
                modres.chain_id = line[16]
                modres.sequence_number = int(line[18:22])
                modres.insertion_code = line[22]
                modres.standard_residue_name = line[24:27]
                modres.comment = line[29:70]

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### HET
        elif record=='HET   ':

            while record=='HET   ':

                het=Het()
                pdb.het.append(het)

                het.het_id = line[7:10]
                het.chain_id = line[12]
                het.sequence_number = int(line[13:17])
                het.insertion_code = line[17]
                het.n_hetatms = int(line[20:25])
                het.description = line[30:70]

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### HETNAM
        elif record=='HETNAM':

            while record=='HETNAM':

                if line[8:10]=='  ':

                    hetnam=Hetnam()
                    pdb.het.append(het)

                    hetnam.het_id = line[11:14]

                hetnam.het_name += line[15:70].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### HETSYN
        elif record=='HETSYN':

            while record=='HETSYN':

                if line[8:10]=='  ':

                    hetnam=Hetnam()
                    pdb.het.append(het)

                    hetnam.het_id = line[11:14]

                hetnam.het_synonyms += [ii.strip() for ii in line[15:70].split(';')]

                counter += 1
                line = lines[counter]
                record = line[0:6]

        ### FORMUL
        elif record=='FORMUL':

            while record=='FORMUL':

                if line[16:18]=='  ':

                    formul=Formul()
                    pdb.formul.append(formul)

                    formul.component_number = int(line[8:10])
                    formul.het_id = line[12:15]
                    if line[18] == '*':
                        formul.water = True

                formul.chemical_formula += line[19:70].strip()

                counter += 1
                line = lines[counter]
                record = line[0:6]





        else:

            counter += 1

        #    raise PDBRecordNotRecognized

    return pdb

