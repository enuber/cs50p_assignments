from seasons import calculate_age_in_minutes
import pytest

def test_seasons():
    assert calculate_age_in_minutes(0) == 'Zero minutes'
    assert calculate_age_in_minutes(365) == 'Five hundred twenty-five thousand, six hundred minutes'
    assert calculate_age_in_minutes(730) == 'One million, fifty-one thousand, two hundred minutes'
