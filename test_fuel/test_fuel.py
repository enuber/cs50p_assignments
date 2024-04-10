from fuel import convert, gauge
import pytest

# // Test the convert function
def test_convert():
    assert convert("1/2") == 50
    assert convert("7/7") == 100

    # // Pytest the convert function (checks for errors)
    with pytest.raises(ValueError):
        convert("two/three")

    with pytest.raises(ZeroDivisionError):
        convert("9/0")

# // Test the gauge function
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(20) == "20%"
