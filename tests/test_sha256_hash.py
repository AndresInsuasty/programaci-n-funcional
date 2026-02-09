"""Unit tests for SHA256 hash function."""

import pytest
from utils.sha256_hash import sha256_hash


def test_sha256_hash_basic():
    """Test SHA256 hash with a basic message."""
    message = "Hello, World!"
    result = sha256_hash(message)
    assert result == "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"


def test_sha256_hash_empty_string():
    """Test SHA256 hash with an empty string."""
    result = sha256_hash("")
    assert result == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def test_sha256_hash_numbers():
    """Test SHA256 hash with numbers."""
    message = "12345"
    result = sha256_hash(message)
    assert result == "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"


def test_sha256_hash_special_characters():
    """Test SHA256 hash with special characters."""
    message = "!@#$%^&*()"
    result = sha256_hash(message)
    assert isinstance(result, str)
    assert len(result) == 64  # SHA256 hash is always 64 hex characters


def test_sha256_hash_unicode():
    """Test SHA256 hash with unicode characters."""
    message = "Hola, ¿cómo estás?"
    result = sha256_hash(message)
    assert isinstance(result, str)
    assert len(result) == 64


def test_sha256_hash_consistent():
    """Test that SHA256 hash produces consistent results."""
    message = "Test message"
    result1 = sha256_hash(message)
    result2 = sha256_hash(message)
    assert result1 == result2
