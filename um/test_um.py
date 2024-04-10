from um import count

# // Test the count function
def test_count():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2
    assert count('U m') == 0
    assert count('mu') == 0
