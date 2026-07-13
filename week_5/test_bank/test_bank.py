from week_5.test_bank.bank import value

def test_saludo_h():
    assert value("hi there") == 20
    assert value("Hi, mister") == 20

def test_saludo_hola():
    assert value("hello how are you?") == 0
    assert value("Hello como se encuentra usted?") == 0

def test_saludo_nada():
    assert value("Whats up men") == 100
    assert value("Men, how you doing?") == 100

