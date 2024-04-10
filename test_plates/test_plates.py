from plates import is_valid

# // Testing the is_valid function
def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("24") == False
    assert is_valid("E") == False
    assert is_valid("DisNeYLand") == False
    assert is_valid("Num32A") == False
    assert is_valid("PI3.14") == False
    assert is_valid("1PIECE") == False
    assert is_valid("ESRB04") == False

