from week_5.test_plates.plates import is_valid


def test_starting_letters():
    assert is_valid("Jorge") == True
    assert is_valid("A1dios") == False
    assert is_valid("22Ner") == False
    assert is_valid("Aa") == True
    assert is_valid("1A") == False
    assert is_valid("11") == False
    assert is_valid("A1") == False

def test_characters():
    assert is_valid("holaaaa") == False
    assert is_valid("J") == False
    assert is_valid("Carro") == True

def test_numbers():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True

def test_punctuation():
    assert is_valid("a.dios") == False
    assert is_valid("#33") == False
    assert is_valid("ner0") == False
    assert is_valid("..") == False
    assert is_valid("CS 50") == False



