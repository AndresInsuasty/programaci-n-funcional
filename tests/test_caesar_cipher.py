"""Unit tests for Caesar cipher function."""

import pytest
from utils.caesar_cipher import caesar_cipher


def test_caesar_cipher_default_shift():
    """Test Caesar cipher with default shift (3)."""
    message = "ABC"
    result = caesar_cipher(message)
    assert result == "DEF"


def test_caesar_cipher_custom_shift():
    """Test Caesar cipher with custom shift."""
    message = "ABC"
    result = caesar_cipher(message, shift=5)
    assert result == "FGH"


def test_caesar_cipher_lowercase():
    """Test Caesar cipher with lowercase letters."""
    message = "abc"
    result = caesar_cipher(message, shift=3)
    assert result == "def"


def test_caesar_cipher_wrap_around():
    """Test Caesar cipher with wrap-around at end of alphabet."""
    message = "XYZ"
    result = caesar_cipher(message, shift=3)
    assert result == "ABC"


def test_caesar_cipher_preserves_non_alpha():
    """Test that Caesar cipher preserves non-alphabetic characters."""
    message = "Hello, World!"
    result = caesar_cipher(message, shift=3)
    assert result == "Khoor, Zruog!"
    

def test_caesar_cipher_mixed_case():
    """Test Caesar cipher with mixed case."""
    message = "HeLLo"
    result = caesar_cipher(message, shift=1)
    assert result == "IfMMp"


def test_caesar_cipher_numbers_unchanged():
    """Test that Caesar cipher leaves numbers unchanged."""
    message = "abc123"
    result = caesar_cipher(message, shift=3)
    assert result == "def123"


def test_caesar_cipher_negative_shift():
    """Test Caesar cipher with negative shift (decryption)."""
    message = "DEF"
    result = caesar_cipher(message, shift=-3)
    assert result == "ABC"


def test_caesar_cipher_zero_shift():
    """Test Caesar cipher with zero shift."""
    message = "Hello, World!"
    result = caesar_cipher(message, shift=0)
    assert result == message
