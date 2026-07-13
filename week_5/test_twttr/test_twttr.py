from week_5.test_twttr.twttr import shorten

def test_vocales_mayus():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("LUIS") == "LS"
    assert shorten("NEREO_RDZ") == "NR_RDZ"



def test_vocales_minus():
    assert shorten("maelena") == "mln"
    assert shorten("olympus") == "lymps"
    assert shorten("west_heights") == "wst_hghts"

def test_vocales_mayus_y_minus():
    assert shorten("Algebra") == "lgbr"
    assert shorten("DAvid") == "Dvd"
    assert shorten("MA_Nuel") == "M_Nl"

def test_puntuacion():
    assert shorten("jj.jorge") == "jj.jrg"
    assert shorten ("lul.lul") == "ll.ll"


def test_numeros():
    assert shorten("J12") == "J12"
    assert shorten ("l22") == "l22"
