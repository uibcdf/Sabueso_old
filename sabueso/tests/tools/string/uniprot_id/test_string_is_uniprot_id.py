"""
Unit and regression test for the tools.string.uniprot.string_id_is_uniprot method of the library sabueso.
"""

# Import package, test suite, and other packages as needed
import sabueso as sab


def test_string_is_uniprot_1():

    is_uniprot = sab.tools.string.uniprot.string_is_uniprot_id('A2BC19')
    assert is_uniprot==True

def test_string_is_uniprot_2():

    is_uniprot = sab.tools.string.uniprot.string_is_uniprot_id('P12345')
    assert is_uniprot==True

def test_string_is_uniprot_3():

    is_uniprot = sab.tools.string.uniprot.string_is_uniprot_id('A0A023GPI8')
    assert is_uniprot==True

def test_string_is_uniprot_4():

    is_uniprot = sab.tools.string.uniprot.string_is_uniprot_id('1BRS')
    assert is_uniprot==False

