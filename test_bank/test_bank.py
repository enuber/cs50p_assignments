from bank import value

def test_correct_words():
    assert value('hello') == 0
    assert value('Howdy') == 20

def test_most_money():
    assert value('what\'s up?') == 100
