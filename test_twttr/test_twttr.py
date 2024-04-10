from twttr import shorten

rv = shorten

def test_words():
    assert rv('word') == 'wrd'
    assert rv('vowels') == 'vwls'

def test_words_without_vowels():
    assert rv('dryly') == 'dryly'
    assert rv('crypt') == 'crypt'

def test_uppercase():
    assert rv('UPPERCASE') == 'PPRCS'

def test_with_numbers():
    assert rv('s0m3th1ng') == 's0m3th1ng'

def test_with_punctation():
    assert rv('egad!') == 'gd!'
