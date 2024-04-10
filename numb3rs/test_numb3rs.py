from numb3rs import validate

def test_valid_addresses():
    assert validate('255.255.255.255') == True
    assert validate('124.56.0.10') == True
    assert validate('0.0.0.0') == True
    assert validate('202.0.10.5') == True
    assert validate('127.0.0.1') == True

def test_invalid_addresses():
    assert validate('256.0.0.0') == False
    assert validate('120.154.0') == False
    assert validate('205..5.10') == False
    assert validate('275.3.6.28') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate("word") == False
    assert validate('75.456.76.65') == False

