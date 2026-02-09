"""Unit tests for Base64 encoding function."""

import pytest
from utils.base64_encode import base64_encode


def test_base64_encode_basic():
    """Test Base64 encoding with a basic message."""
    message = "Hello, World!"
    result = base64_encode(message)
    assert result == "SGVsbG8sIFdvcmxkIQ=="


def test_base64_encode_empty_string():
    """Test Base64 encoding with an empty string."""
    result = base64_encode("")
    assert result == ""


def test_base64_encode_numbers():
    """Test Base64 encoding with numbers."""
    message = "12345"
    result = base64_encode(message)
    assert result == "MTIzNDU="


def test_base64_encode_special_characters():
    """Test Base64 encoding with special characters."""
    message = "!@#$%^&*()"
    result = base64_encode(message)
    assert isinstance(result, str)
    # Verify it's valid Base64 (only contains valid Base64 characters)
    assert all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in result)


def test_base64_encode_unicode():
    """Test Base64 encoding with unicode characters."""
    message = "Hola, ¿cómo estás?"
    result = base64_encode(message)
    assert isinstance(result, str)
    assert all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in result)


def test_base64_encode_long_text():
    """Test Base64 encoding with long text."""
    message = "This is a longer message that will be encoded using Base64."
    result = base64_encode(message)
    assert isinstance(result, str)
    assert len(result) > len(message)  # Base64 encoding increases size
