import urllib as _urllib
import xmltodict as _xmltodict
from copy import deepcopy as _deepcopy
from sabueso.fields.protein import in_pdb_card as _in_pdb_card
from sabueso.fields.protein import segment_card as _segment_card

def target_query(string=None, organism=None, max_results=20):

    url = 'http://www.uniprot.org/uniprot/?query='+string+'&format=xml&limit='+str(max_results)+'&sort=score'
    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/Sabueso || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)

    list_results=[]
    for entry in dict_result['uniprot']['entry']:
        list_results.append(_parse_basic_entry(entry))

    return list_results

def _get_organism_scientific(uniprot_id=None):

    url = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.xml'
    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/Sabueso || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)
    dict_result = dict_result['uniprot']['entry']
    tmp_name = None

    if 'organism' in dict_result.keys():
        if type(dict_result['organism']['name'])==list:
            for name in dict_result['organism']['name']:
                if name['@type']=='scientific':
                    tmp_name=name['#text']

    del(url,request,response,xml_result,dict_result)
    return tmp_name

def _get_FASTA(uniprot_id=None):

    url_fasta = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.fasta'
    request_fasta = _urllib.request.Request(url_fasta)
    request_fasta.add_header('User-Agent', 'Python at https://github.com/uibcdf/Sabueso || prada.gracia@gmail.com')
    response_fasta = _urllib.request.urlopen(request_fasta)
    fasta_result = response_fasta.read().decode('utf-8')

    del(url_fasta,request_fasta,response_fasta)

    return fasta_result

def _get_GFF(uniprot_id=None):

    url_gff = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.gff'
    request_gff = _urllib.request.Request(url_gff)
    request_gff.add_header('User-Agent', 'Python at https://github.com/uibcdf/Sabueso || prada.gracia@gmail.com')
    response_gff = _urllib.request.urlopen(request_gff)
    gff_result = response_gff.read().decode('utf-8')

    del(url_gff,request_gff,response_gff)

    return gff_result

def _parse_GFF(GFF):

    tmp_lines = GFF.split('\n')

    to_chains={}
    to_domains={}
    to_regions={}
    to_motifs={}
    to_mutagenesis={}
    to_modified={}
    to_crosslink={}
    to_altseq={}
    to_seqconf={}
    tmp_num_chains=0
    tmp_num_domains=0
    tmp_num_regions=0
    tmp_num_motifs=0
    tmp_num_mutagenesis=0
    tmp_num_modified=0
    tmp_num_crosslink=0
    tmp_num_seqconf=0
    tmp_num_altseq=0

    from sabueso.fields.protein import domain_card as _domain_card
    from sabueso.fields.protein import chain_card as _chain_card
    from sabueso.fields.protein import region_card as _region_card
    from sabueso.fields.protein import motif_card as _motif_card
    from sabueso.fields.protein import mutagenesis_card as _mutagenesis_card
    from sabueso.fields.protein import modified_res_card as _modified_res_card
    from sabueso.fields.protein import cross_link_card as _cross_link_card
    from sabueso.fields.protein import alternative_seq_card as _alternative_seq_card
    from sabueso.fields.protein import seq_conflict_card as _seq_conflict_card

    for line in tmp_lines[2:]:
        fields_line = line.split('\t')
        if len(fields_line)>1:
            if fields_line[2]=='Chain':
                tmp_chain = _deepcopy(_chain_card)
                tmp_chain['Begin'] = int(fields_line[3])
                tmp_chain['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_chain['Description'] = ii.replace('Note=','')
                to_chains[tmp_num_chains]=tmp_chain
                tmp_num_chains+=1
                del(tmp_chain,tmp_txt)
            if fields_line[2]=='Domain':
                tmp_domain = _deepcopy(_domain_card)
                tmp_domain['Begin'] = int(fields_line[3])
                tmp_domain['End'] = int(fields_line[4])
                tmp_break = fields_line[8].split('|')
                if tmp_break[-1].startswith('PROSITE'):
                    tmp_domain['PROSITE-ProRule'] = tmp_break[-1].split('=')[-1]
                tmp_txt=tmp_break[0].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_domain['Name'] = ii.replace('Note=','')
                to_domains[tmp_num_domains]=tmp_domain
                tmp_num_domains+=1
                del(tmp_domain,tmp_break,tmp_txt)
            if fields_line[2]=='Region':
                tmp_region = _deepcopy(_region_card)
                tmp_region['Begin'] = int(fields_line[3])
                tmp_region['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_region['Name'] = ii.replace('Note=','')
                to_regions[tmp_num_regions]=tmp_region
                tmp_num_regions+=1
                del(tmp_region,tmp_txt)
            if fields_line[2]=='Motif':
                tmp_motif = _deepcopy(_motif_card)
                tmp_motif['Begin'] = int(fields_line[3])
                tmp_motif['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_motif['Name'] = ii.replace('Note=','')
                to_motifs[tmp_num_motifs]=tmp_motif
                tmp_num_motifs+=1
                del(tmp_motif,tmp_txt)
            if fields_line[2]=='Mutagenesis':
                tmp_mutagenesis = _deepcopy(_mutagenesis_card)
                tmp_mutagenesis['Begin'] = int(fields_line[3])
                tmp_mutagenesis['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_mutagenesis['Description'] = ii.replace('Note=','')
                to_mutagenesis[tmp_num_mutagenesis]=tmp_mutagenesis
                tmp_num_mutagenesis+=1
                del(tmp_mutagenesis,tmp_txt)
            if fields_line[2]=='Modified residue':
                tmp_modified = _deepcopy(_modified_res_card)
                tmp_modified['Begin'] = int(fields_line[3])
                tmp_modified['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_modified['Description'] = ii.replace('Note=','')
                to_modified[tmp_num_modified]=tmp_modified
                tmp_num_modified+=1
                del(tmp_modified,tmp_txt)
            if fields_line[2]=='Cross-link':
                tmp_crosslink = _deepcopy(_cross_link_card)
                tmp_crosslink['Begin'] = int(fields_line[3])
                tmp_crosslink['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_crosslink['Description'] = ii.replace('Note=','')
                to_crosslink[tmp_num_crosslink]=tmp_crosslink
                tmp_num_crosslink+=1
                del(tmp_crosslink,tmp_txt)
            if fields_line[2]=='Alternative sequence':
                tmp_altseq = _deepcopy(_alternative_seq_card)
                tmp_altseq['Begin'] = int(fields_line[3])
                tmp_altseq['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_altseq['Description'] = ii.replace('Note=','')
                to_altseq[tmp_num_altseq]=tmp_altseq
                tmp_num_altseq+=1
                del(tmp_altseq,tmp_txt)
            if fields_line[2]=='Sequence conflict':
                tmp_seqconf = _deepcopy(_seq_conflict_card)
                tmp_seqconf['Begin'] = int(fields_line[3])
                tmp_seqconf['End'] = int(fields_line[4])
                tmp_txt=fields_line[8].split(';')
                for ii in tmp_txt:
                    if ii.startswith('Note='):
                        tmp_seqconf['Description'] = ii.replace('Note=','')
                to_seqconf[tmp_num_seqconf]=tmp_seqconf
                tmp_num_seqconf+=1
                del(tmp_seqconf,tmp_txt)

    return to_chains,to_domains,to_regions,to_motifs,to_mutagenesis,to_modified,\
           to_crosslink,to_altseq,to_seqconf

def _get_sequence_from_FASTA(FASTA=None):

    tmp_lines = FASTA.split('\n')
    return ''.join(tmp_lines[1:])

def _parse_basic_entry(entry=None, card=None):

    dict_result=entry

    if card is None:
        from sabueso.fields.protein import protein_card as _protein_card
        tmp_card = _deepcopy(_protein_card)
        del(_protein_card)
    else:
        tmp_card = card

    # Name
    tmp_card['Name'].append(dict_result['name'])

    # Full Name
    if 'recommendedName' in dict_result['protein'].keys():
        if 'fullName' in dict_result['protein']['recommendedName'].keys():
            if type(dict_result['protein']['recommendedName']['fullName'])!=str:
                tmp_card['Full Name'].append(dict_result['protein']['recommendedName']['fullName']['#text'])
            else:
                tmp_card['Full Name'].append(dict_result['protein']['recommendedName']['fullName'])
    # Short Name
        if 'shortName' in dict_result['protein']['recommendedName'].keys():
            if type(dict_result['protein']['recommendedName']['shortName'])==list:
                for shortName in dict_result['protein']['recommendedName']['shortName']:
                    if type(shortName)==str:
                        tmp_card['Short Name'].append(shortName)
                    else:
                        tmp_card['Short Name'].append(shortName['#text'])
            else:
                tmp_card['Short Name'].append(dict_result['protein']['recommendedName']['shortName'])

    # Alternative Name
    if 'alternativeName' in dict_result['protein'].keys():
        if type(dict_result['protein']['alternativeName'])==list:
            for alternativeName in dict_result['protein']['alternativeName']:
                if type(alternativeName['fullName'])==str:
                    tmp_card['Alternative Name'].append(alternativeName['fullName'])
                else:
                    tmp_card['Alternative Name'].append(alternativeName['fullName']['#text'])
        else:
            tmp_card['Alternative Name'].append(dict_result['protein']['alternativeName']['fullName'])

    # Type
    tmp_card['Type'].append('Protein')

    # Organism
    if 'organism' in dict_result.keys():
        if type(dict_result['organism']['name'])==list:
            for name in dict_result['organism']['name']:
                if name['@type']=='scientific':
                    tmp_card['Organism Scientific'].append(name['#text'])
                if name['@type']=='common':
                    tmp_card['Organism'].append(name['#text'])
        else:
            tmp_card['Organism'].append(dict_result['organism']['name']['#text'])

    # Host
    if 'organismHost' in dict_result.keys():
        tmp_card['Host'].append(dict_result['organismHost']['name'][0]['#text'])

    # Uniprot

    if type(dict_result['accession'])== list:
        for ii in dict_result['accession']:
            tmp_card['UniProt'].append(ii)
    else:
        tmp_card['UniProt'].append(dict_result['accession'])

    # Sequence
    tmp_card['Sequence']['Canonical']=dict_result['sequence']['#text'].replace('\n','')


    for dbreference in dict_result['dbReference']:

    # ChEMBL
        if dbreference['@type']=='ChEMBL':
            tmp_card['ChEMBL'].append(dbreference['@id'])

    # BioGRID
        elif dbreference['@type']=='BioGRID':
            tmp_card['BioGRID'].append(dbreference['@id'])

    # Protein Model Portal
        elif dbreference['@type']=='ProteinModelPortal':
            tmp_card['ProteinModelPortal'].append(dbreference['@id'])

    # Swiss Model
        elif dbreference['@type']=='SMR':
            tmp_card['Swiss-Model'].append(dbreference['@id'])

    # DIP
        elif dbreference['@type']=='DIP':
            tmp_card['DIP'].append(dbreference['@id'])

    # ELM
        elif dbreference['@type']=='ELM':
            tmp_card['ELM'].append(dbreference['@id'])

    # IntAct
        elif dbreference['@type']=='IntAct':
            tmp_card['IntAct'].append(dbreference['@id'])

    # MINT
        elif dbreference['@type']=='MINT':
            tmp_card['MINT'].append(dbreference['@id'])

    # BindingDB
        elif dbreference['@type']=='BindingDB':
            tmp_card['BindingDB'].append(dbreference['@id'])

    # InterPro
        elif dbreference['@type']=='InterPro':
            tmp_card['InterPro'].append(dbreference['@id'])

    # Pfam
        elif dbreference['@type']=='Pfam':
            tmp_card['Pfam'].append(dbreference['@id'])

    # ProDom
        elif dbreference['@type']=='ProDom':
            tmp_card['ProDom'].append(dbreference['@id'])

    # SUPFAM
        elif dbreference['@type']=='SUPFAM':
            tmp_card['SUPFAM'].append(dbreference['@id'])

    # STRING
        elif dbreference['@type']=='STRING':
            tmp_card['STRING'].append(dbreference['@id'])

    # iPTMnet
        elif dbreference['@type']=='iPTMnet':
            tmp_card['iPTMnet'].append(dbreference['@id'])

    # PhosphoSitePlus
        elif dbreference['@type']=='PhosphoSitePlus':
            tmp_card['PhosphoSitePlus'].append(dbreference['@id'])

    # PDBs
        elif dbreference['@type']=='PDB':
            tmp_pdb_id=dbreference['@id']
            for pdb_field in dbreference['property']:
                if pdb_field['@type']=='chains':
                    tmp_in_pdb_card=_deepcopy(_in_pdb_card)
                    tmp_segments=pdb_field['@value'].split(',')
                    tmp_in_pdb_card['Id']=tmp_pdb_id
                    for tmp_segment in tmp_segments:
                        tmp_terms_segment=tmp_segment.split('=')
                        tmp_chains_segment=tmp_terms_segment[0]
                        tmp_nums_segment=tmp_terms_segment[1].split('-')
                        tmp_begin=int(tmp_nums_segment[0])
                        tmp_end=int(tmp_nums_segment[1])
                        for tmp_chain_segment in tmp_chains_segment.split('/'):
                            tmp_segment_card=_deepcopy(_segment_card)
                            tmp_segment_card['Chain']=tmp_chain_segment
                            tmp_segment_card['Begin']=tmp_begin
                            tmp_segment_card['End']=tmp_end
                            tmp_segment_card['Length']=tmp_end-tmp_begin+1
                            tmp_in_pdb_card['Segment'].append(tmp_segment_card)
                        del(tmp_terms_segment,tmp_chains_segment,tmp_nums_segment)
                        del(tmp_begin,tmp_end)
                    tmp_card['in PDB'][tmp_pdb_id]=tmp_in_pdb_card
                    del(tmp_in_pdb_card)
            del(tmp_pdb_id)

    return tmp_card


def protein_card(uniprot_id=None, card=None, with_interactions=True, with_FASTA=True):

    url = 'http://www.uniprot.org/uniprot/'+uniprot_id+'.xml'

    request = _urllib.request.Request(url)
    request.add_header('User-Agent', 'Python at https://github.com/uibcdf/Sabueso || prada.gracia@gmail.com')
    response = _urllib.request.urlopen(request)
    xml_result = response.read().decode('utf-8')
    dict_result = _xmltodict.parse(xml_result)
    dict_result = dict_result['uniprot']['entry']

    tmp_card = _parse_basic_entry(dict_result)

    # FASTA
    tmp_card['Sequence']['FASTA']=_get_FASTA(uniprot_id)

    # Function
    # Subunit Structure
    # Interactions
    # Isoforms
    if type(dict_result['comment'])== list:
        for comment in dict_result['comment']:

            if comment['@type']=='function':
                if type(comment['text'])==list:
                    for function in comment['text']:
                            tmp_card['Function'].append(function['#text'])
                else:
                    try:
                        tmp_card['Function'].append(comment['text']['#text'])
                    except:
                        tmp_card['Function'].append(comment['text'])

            if comment['@type']=='subunit':
                if type(comment['text'])==list:
                    for function in comment['text']:
                            tmp_card['Subunit Structure'].append(function['#text'])
                else:
                    try:
                        tmp_card['Subunit Structure'].append(comment['text']['#text'])
                    except:
                        tmp_card['Subunit Structure'].append(comment['text'])

            if comment['@type']=='alternative products':
                from sabueso.fields.protein import isoform_card as _isoform_card
                if type(comment['isoform'])==list:
                    for isoform in comment['isoform']:
                        tmp_isoform = _deepcopy(_isoform_card)
                        tmp_isoform['Name'] =  isoform['name']
                        tmp_isoform_indice = int(isoform['id'].split('-')[-1])
                        tmp_isoform['FASTA'] = _get_FASTA(isoform['id'])
                        tmp_isoform['Sequence'] = _get_sequence_from_FASTA(tmp_isoform['FASTA'])
                        tmp_isoform['UniProt'] = isoform['id']
                        tmp_card['Sequence']['Isoforms'][tmp_isoform_indice]=tmp_isoform
                        del(tmp_isoform_indice)
                else:
                    isoform = comment['isoform']
                    tmp_isoform = _deepcopy(_isoform_card)
                    tmp_isoform['Name'] =  isoform['name']
                    tmp_isoform_indice = int(isoform['id'].split('-')[-1])
                    tmp_isoform['FASTA'] = _get_FASTA(isoform['id'])
                    tmp_isoform['Sequence'] = _get_sequence_from_FASTA(tmp_isoform['FASTA'])
                    tmp_isoform['UniProt'] = isoform['id']
                    tmp_card['Sequence']['Isoforms'][tmp_isoform_indice]=tmp_isoform
                    del(tmp_isoform_indice)
                del(_isoform_card)

            if with_interactions:
                if comment['@type']=='interaction':
                    from sabueso.fields.interaction import interaction_card as _interaction_card
                    tmp_interaction = _deepcopy(_interaction_card)
                    tmp_interactant=tmp_interaction['Interactants'][0]
                    tmp_interactant['UniProt']=uniprot_id
                    tmp_interactant['IntAct']=comment['interactant'][0]['@intactId']
                    tmp_interactant['Organism Scientific']=tmp_card['Organism Scientific'][0]
                    tmp_interactant['Short Name']=tmp_card['Short Name']
                    tmp_interactant=tmp_interaction['Interactants'][1]
                    tmp_interactant['UniProt']=comment['interactant'][1]['id']
                    tmp_interactant['IntAct']=comment['interactant'][1]['@intactId']
                    tmp_interactant['Short Name']=comment['interactant'][1]['label']
                    if comment['organismsDiffer']=='false':
                        tmp_interactant['Organism']=tmp_card['Organism Scientific'][0]
                    else:
                        tmp_uniprot = comment['interactant'][1]['id']
                        tmp_organism = _get_organism_scientific(tmp_uniprot)
                        tmp_interactant['Organism Scientific']=tmp_organism
                        del(tmp_uniprot,tmp_organism)
                    tmp_card['Interactions'].append(tmp_interaction)
                    del(tmp_interaction,tmp_interactant,_interaction_card)
    else:
        if dict_result['comment']['@type']=='function':
            tmp_card['Function'].append(dict_result['comment']['text'])
        if dict_result['comment']['@type']=='subunit':
            tmp_card['Subunit Structure'].append(dict_result['comment']['text'])

    # Fix lack of isoforms where number of isoforms == 1:

    if len(tmp_card['Sequence']['Isoforms'])==0:
        from sabueso.fields.protein import isoform_card as _isoform_card
        tmp_isoform = _deepcopy(_isoform_card)
        tmp_isoform['Name'] =  str(1)
        tmp_isoform_indice = 1
        tmp_isoform['UniProt'] = tmp_card['UniProt'][0]+'-1'
        tmp_isoform['FASTA'] = _get_FASTA(tmp_isoform['UniProt'])
        tmp_isoform['Sequence'] = _get_sequence_from_FASTA(tmp_isoform['FASTA'])
        tmp_card['Sequence']['Isoforms'][tmp_isoform_indice]=tmp_isoform
        del(tmp_isoform_indice,_isoform_card)

    # Structure
    # Domains

    tmp_gff =_get_GFF(uniprot_id)
    to_chains,to_domains,to_regions,to_motifs,to_mutagenesis,to_modified,\
    to_crosslink,to_altseq,to_seqconf = _parse_GFF(tmp_gff)

    tmp_card['Structure']['Chain']=to_chains
    tmp_card['Structure']['Domain']=to_domains
    tmp_card['Structure']['Region']=to_regions
    tmp_card['Structure']['Motif']=to_motifs

    tmp_card['Sequence']['PostTranslational Modifications']['Modified Residues']=to_modified
    tmp_card['Sequence']['PostTranslational Modifications']['Cross-link']=to_crosslink
    tmp_card['Sequence']['Sequence Conflict']=to_seqconf
    tmp_card['Sequence']['Alternative Sequence']=to_altseq

    tmp_card['Experimental Evidences']['Mutagenesis']=to_mutagenesis

    del(to_chains,to_domains,to_regions,to_motifs,to_mutagenesis,to_modified,\
        to_crosslink,to_altseq,to_seqconf)
    del(url, request, response, xml_result, dict_result)
    del(tmp_gff)

    return tmp_card

