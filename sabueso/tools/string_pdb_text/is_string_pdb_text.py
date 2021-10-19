
def is_string_pdb_text(item):

    import re

    pattern_1 = r'((ATOM||HETATM)+\s+\d+\s+\w+\s+\w+\s+\w+\s+\d+(\s+[+-]?([0-9]+([.][0-9]*))){5})'
    pattern_2 = r'((ATOM||HETATM)+\s+\d+\s+\w+\s+\w+\s+\w+\s+(\s+[+-]?([0-9]+([.][0-9]*))){5})'

    for pattern in [pattern_1, pattern_2]:

        n_good_lines = len(re.findall(pattern, item))
        output = (n_good_lines>0)

        if output:
            break

    return output

