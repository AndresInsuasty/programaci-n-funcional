"""Pruebas unitarias para la función de cifrado ROT13."""

import pytest
from utils.rot13_cipher import rot13_cipher


def test_rot13_cipher_basic():
    """Prueba cifrado ROT13 con texto básico."""
    message = "Hello"
    result = rot13_cipher(message)
    assert result == "Uryyb"


def test_rot13_cipher_full_alphabet():
    """Prueba cifrado ROT13 con alfabeto completo."""
    message = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = rot13_cipher(message)
    assert result == "NOPQRSTUVWXYZABCDEFGHIJKLM"


def test_rot13_cipher_lowercase():
    """Prueba cifrado ROT13 con letras minúsculas."""
    message = "abcdefghijklmnopqrstuvwxyz"
    result = rot13_cipher(message)
    assert result == "nopqrstuvwxyzabcdefghijklm"


def test_rot13_cipher_preserves_non_alpha():
    """Prueba que cifrado ROT13 preserva caracteres no alfabéticos."""
    message = "Hello, World!"
    result = rot13_cipher(message)
    assert result == "Uryyb, Jbeyq!"


def test_rot13_cipher_double_application():
    """Prueba que aplicar ROT13 dos veces devuelve el mensaje original."""
    message = "Hello, World!"
    encrypted = rot13_cipher(message)
    decrypted = rot13_cipher(encrypted)
    assert decrypted == message


def test_rot13_cipher_numbers_unchanged():
    """Prueba que cifrado ROT13 deja los números sin cambios."""
    message = "abc123"
    result = rot13_cipher(message)
    assert result == "nop123"


def test_rot13_cipher_mixed_content():
    """Prueba cifrado ROT13 con contenido mezclado."""
    message = "Test123!@# Message"
    result = rot13_cipher(message)
    assert result == "Grfg123!@# Zrffntr"


def test_rot13_cipher_empty_string():
    """Prueba cifrado ROT13 con cadena vacía."""
    message = ""
    result = rot13_cipher(message)
    assert result == ""
