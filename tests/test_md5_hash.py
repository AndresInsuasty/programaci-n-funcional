"""Unit tests for MD5 hash function."""

import pytest
from utils.md5_hash import md5_hash


def test_md5_hash_basic():
    """Test MD5 hash with a basic message."""
    message = "Hello, World!"
    result = md5_hash(message)
    assert result == "65a8e27d8879283831b664bd8b7f0ad4"


def test_md5_hash_empty_string():
    """Test MD5 hash with an empty string."""
    result = md5_hash("")
    assert result == "d41d8cd98f00b204e9800998ecf8427e"


def test_md5_hash_numbers():
    """Test MD5 hash with numbers."""
    message = "12345"
    result = md5_hash(message)
    assert result == "827ccb0eea8a706c4c34a16891f84e7b"


def test_md5_hash_special_characters():
    """Test MD5 hash with special characters."""
    message = "!@#$%^&*()"
    result = md5_hash(message)
    assert isinstance(result, str)
    assert len(result) == 32  # MD5 hash is always 32 hex characters


def test_md5_hash_unicode():
    """Test MD5 hash with unicode characters."""
    message = "Hola, ¿cómo estás?"
    result = md5_hash(message)
    assert isinstance(result, str)
    assert len(result) == 32


def test_md5_hash_consistent():
    """Test that MD5 hash produces consistent results."""
    message = "Test message"
    result1 = md5_hash(message)
    result2 = md5_hash(message)
    assert result1 == result2
