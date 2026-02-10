"""Pruebas unitarias para la función de codificación Base64."""

import pytest
from utils.base64_encode import base64_encode


def test_base64_encode_basic():
    """Prueba codificación Base64 con un mensaje básico."""
    message = "Hello, World!"
    result = base64_encode(message)
    assert result == "SGVsbG8sIFdvcmxkIQ=="


def test_base64_encode_empty_string():
    """Prueba codificación Base64 con una cadena vacía."""
    result = base64_encode("")
    assert result == ""


def test_base64_encode_numbers():
    """Prueba codificación Base64 con números."""
    message = "12345"
    result = base64_encode(message)
    assert result == "MTIzNDU="


def test_base64_encode_special_characters():
    """Prueba codificación Base64 con caracteres especiales."""
    message = "!@#$%^&*()"
    result = base64_encode(message)
    assert isinstance(result, str)
    # Verificar que es Base64 válido (solo contiene caracteres Base64 válidos)
    assert all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in result)


def test_base64_encode_unicode():
    """Prueba codificación Base64 con caracteres unicode."""
    message = "Hola, ¿cómo estás?"
    result = base64_encode(message)
    assert isinstance(result, str)
    assert all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=" for c in result)


def test_base64_encode_long_text():
    """Prueba codificación Base64 con texto largo."""
    message = "This is a longer message that will be encoded using Base64."
    result = base64_encode(message)
    assert isinstance(result, str)
    assert len(result) > len(message)  # Codificación Base64 incrementa el tamaño
