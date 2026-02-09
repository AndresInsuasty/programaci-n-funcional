"""Unit tests for ROT13 cipher function."""

import pytest
from utils.rot13_cipher import rot13_cipher


def test_rot13_cipher_basic():
    """Test ROT13 cipher with basic text."""
    message = "Hello"
    result = rot13_cipher(message)
    assert result == "Uryyb"


def test_rot13_cipher_full_alphabet():
    """Test ROT13 cipher with full alphabet."""
    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = rot13_cipher(message)
    assert result == "NOPQRSTUVWXYZABCDEFGHIJKLM"


def test_rot13_cipher_lowercase():
    """Test ROT13 cipher with lowercase letters."""
    message = "abcdefghijklmnopqrstuvwxyz"
    result = rot13_cipher(message)
    assert result == "nopqrstuvwxyzabcdefghijklm"


def test_rot13_cipher_preserves_non_alpha():
    """Test that ROT13 cipher preserves non-alphabetic characters."""
    message = "Hello, World!"
    result = rot13_cipher(message)
    assert result == "Uryyb, Jbeyq!"


def test_rot13_cipher_double_application():
    """Test that applying ROT13 twice returns the original message."""
    message = "Hello, World!"
    encrypted = rot13_cipher(message)
    decrypted = rot13_cipher(encrypted)
    assert decrypted == message


def test_rot13_cipher_numbers_unchanged():
    """Test that ROT13 cipher leaves numbers unchanged."""
    message = "abc123"
    result = rot13_cipher(message)
    assert result == "nop123"


def test_rot13_cipher_mixed_content():
    """Test ROT13 cipher with mixed content."""
    message = "Test123!@# Message"
    result = rot13_cipher(message)
    assert result == "Grfg123!@# Zrffntr"


def test_rot13_cipher_empty_string():
    """Test ROT13 cipher with empty string."""
    message = ""
    result = rot13_cipher(message)
    assert result == ""
