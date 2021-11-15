"""
Unit and regression test for the tools.string.uniprot.string_id_is_uniprot method of the library sabueso.
"""

# Import package, test suite, and other packages as needed
import sabueso as sab


def test_string_is_uniprot_1():

    output = sab.tools.string_uniprot_id.is_string_uniprot_id('A2BC19')
    assert output==True

def test_string_is_uniprot_2():

    output = sab.tools.string_uniprot_id.is_string_uniprot_id('P12345')
    assert output==True

def test_string_is_uniprot_3():

    output = sab.tools.string_uniprot_id.is_string_uniprot_id('A0A023GPI8')
    assert output==True

def test_string_is_uniprot_4():

    output = sab.tools.string_uniprot_id.is_string_uniprot_id('1BRS')
    assert output==False

