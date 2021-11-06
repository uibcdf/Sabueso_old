import nbformat as nbf

def _seq_to_block(sequence, length=80):

    output = ''

    for ii in range(0, len(sequence), length):
        output += sequence[ii:length+ii]+'\n'

    return output

def notebook(card):

    nb = nbf.v4.new_notebook()

    # Title

    text = f"# **Function Card** (*{card.protein_name.value}, {card.organism_common_name.value}*)"

    cell_title = nbf.v4.new_markdown_cell(text)

    ## Uniprot function

    text = f"""\
### UniProtKB function

{card.uniprot_function}

{card.notes}

{card.references}
"""

    cell_uniprot_function = nbf.v4.new_markdown_cell(text)

    ###############

    nb['cells'] = [cell_title, cell_uniprot_function]

    return nb

