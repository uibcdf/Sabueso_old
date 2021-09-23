"""
Unit and regression test for the tools.string.pdb_id.string_is_pdb_id method of the library sabueso.
"""

# Import package, test suite, and other packages as needed
import sabueso as sab


def test_string_is_pdb_id_1():

    is_pdbid = sab.tools.string.pdbid.string_is_pdbid('1BRS')
    assert is_pdbid==True

def test_string_is_pdb_id_2():

    is_pdbid = sab.tools.string.pdbid.string_is_pdbid('X3BD')
    assert is_pdbid==False

def test_string_is_pdb_id_3():

    is_pdbid = sab.tools.string.pdbid.string_is_pdbid('P00648')
    assert is_pdbid==False

