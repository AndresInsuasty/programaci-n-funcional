"""Pruebas unitarias para la función de hash MD5."""

import pytest
from utils.md5_hash import md5_hash


def test_md5_hash_basic():
    """Prueba hash MD5 con un mensaje básico."""
    message = "Hello, World!"
    result = md5_hash(message)
    assert result == "65a8e27d8879283831b664bd8b7f0ad4"


def test_md5_hash_empty_string():
    """Prueba hash MD5 con una cadena vacía."""
    result = md5_hash("")
    assert result == "d41d8cd98f00b204e9800998ecf8427e"


def test_md5_hash_numbers():
    """Prueba hash MD5 con números."""
    message = "12345"
    result = md5_hash(message)
    assert result == "827ccb0eea8a706c4c34a16891f84e7b"


def test_md5_hash_special_characters():
    """Prueba hash MD5 con caracteres especiales."""
    message = "!@#$%^&*()"
    result = md5_hash(message)
    assert isinstance(result, str)
    assert len(result) == 32  # Hash MD5 siempre es de 32 caracteres hexadecimales


def test_md5_hash_unicode():
    """Prueba hash MD5 con caracteres unicode."""
    message = "Hola, ¿cómo estás?"
    result = md5_hash(message)
    assert isinstance(result, str)
    assert len(result) == 32


def test_md5_hash_consistent():
    """Prueba que hash MD5 produce resultados consistentes."""
    message = "Test message"
    result1 = md5_hash(message)
    result2 = md5_hash(message)
    assert result1 == result2
