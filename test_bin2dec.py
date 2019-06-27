import pytest

from bin2dec import to_dec


@pytest.mark.parametrize("test_input,expected", [
    ('0b0', 0),
    ('0b1', 1),
    ('0b10', 2),
    ('0b11', 3),
    ('0b101', 5),
    ('0b110', 6),
    ('0b111', 7),
    ('0b1000', 8),
    ('0b1001', 9),
])


def test_to_dec(test_input, expected):
    assert to_dec(test_input) == expected


def test_to_dec_not_bin_start():
    with pytest.raises(TypeError):
        to_dec('01010101')


def test_to_dec_not_bin_value():
    with pytest.raises(ValueError):
        to_dec('0b12345')


def test_to_dec_empty_bin():
    with pytest.raises(ValueError):
        to_dec('0b')

