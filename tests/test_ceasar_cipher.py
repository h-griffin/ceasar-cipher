from ceasar_cipher import __version__
from ceasar_cipher.ceasar_cipher import encrypt, decrypt, hack

def test_version():
    assert __version__ == '0.1.0'

def test_upper():
    actual = encrypt('ABC', 1)
    expected = 'BCD'
    assert actual == expected

def test_lower():
    actual = encrypt('abc', 1)
    expected = 'bcd'
    assert actual == expected

def test_special():
    actual = encrypt('a-B-c', 1)
    expected = 'b-C-d'
    assert actual == expected

def test_whitespace():
    actual = encrypt('a b c', 1)
    expected = 'b c d'
    assert actual == expected

def test_hack():
    secret = encrypt('It was the best of times, it was the worst of times.', 5)
    actual = hack(secret)
    expected = 'It was the best of times, it was the worst of times.'





