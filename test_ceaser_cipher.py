from ceaser_cipher import encrypt, decrypt, crack
import pytest

text = "It was the best of times, it was the worst of times."
encoded = "Ny bfx ymj gjxy tk ynrjx, ny bfx ymj btwxy tk ynrjx."

def test_encrypt():
    actual = encrypt(text)
    expected = "Ny bfx ymj gjxy tk ynrjx, ny bfx ymj btwxy tk ynrjx."
    assert actual == expected

def test_decrypt():
    actual = decrypt(encoded)
    expected = "It was the best of times, it was the worst of times."
    assert actual == expected
