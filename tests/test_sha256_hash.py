"""Pruebas unitarias para la función de hash SHA256."""

import pytest
from utils.sha256_hash import sha256_hash


def test_sha256_hash_basic():
    """Prueba hash SHA256 con un mensaje básico."""
    message = "Hello, World!"
    result = sha256_hash(message)
    assert result == "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f"


def test_sha256_hash_empty_string():
    """Prueba hash SHA256 con una cadena vacía."""
    result = sha256_hash("")
    assert result == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"


def test_sha256_hash_numbers():
    """Prueba hash SHA256 con números."""
    message = "12345"
    result = sha256_hash(message)
    assert result == "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"


def test_sha256_hash_special_characters():
    """Prueba hash SHA256 con caracteres especiales."""
    message = "!@#$%^&*()"
    result = sha256_hash(message)
    assert isinstance(result, str)
    assert len(result) == 64  # Hash SHA256 siempre es de 64 caracteres hexadecimales


def test_sha256_hash_unicode():
    """Prueba hash SHA256 con caracteres unicode."""
    message = "Hola, ¿cómo estás?"
    result = sha256_hash(message)
    assert isinstance(result, str)
    assert len(result) == 64


def test_sha256_hash_consistent():
    """Prueba que hash SHA256 produce resultados consistentes."""
    message = "Test message"
    result1 = sha256_hash(message)
    result2 = sha256_hash(message)
    assert result1 == result2
