"""Pruebas unitarias para la función de cifrado César."""

import pytest
from utils.caesar_cipher import caesar_cipher


def test_caesar_cipher_default_shift():
    """Prueba cifrado César con desplazamiento por defecto (3)."""
    message = "ABC"
    result = caesar_cipher(message)
    assert result == "DEF"


def test_caesar_cipher_custom_shift():
    """Prueba cifrado César con desplazamiento personalizado."""
    message = "ABC"
    result = caesar_cipher(message, shift=5)
    assert result == "FGH"


def test_caesar_cipher_lowercase():
    """Prueba cifrado César con letras minúsculas."""
    message = "abc"
    result = caesar_cipher(message, shift=3)
    assert result == "def"


def test_caesar_cipher_wrap_around():
    """Prueba cifrado César con envolvimiento al final del alfabeto."""
    message = "XYZ"
    result = caesar_cipher(message, shift=3)
    assert result == "ABC"


def test_caesar_cipher_preserves_non_alpha():
    """Prueba que cifrado César preserva caracteres no alfabéticos."""
    message = "Hello, World!"
    result = caesar_cipher(message, shift=3)
    assert result == "Khoor, Zruog!"
    

def test_caesar_cipher_mixed_case():
    """Prueba cifrado César con mezcla de mayúsculas y minúsculas."""
    message = "HeLLo"
    result = caesar_cipher(message, shift=1)
    assert result == "IfMMp"


def test_caesar_cipher_numbers_unchanged():
    """Prueba que cifrado César deja los números sin cambios."""
    message = "abc123"
    result = caesar_cipher(message, shift=3)
    assert result == "def123"


def test_caesar_cipher_negative_shift():
    """Prueba cifrado César con desplazamiento negativo (descifrado)."""
    message = "DEF"
    result = caesar_cipher(message, shift=-3)
    assert result == "ABC"


def test_caesar_cipher_zero_shift():
    """Prueba cifrado César con desplazamiento cero."""
    message = "Hello, World!"
    result = caesar_cipher(message, shift=0)
    assert result == message
