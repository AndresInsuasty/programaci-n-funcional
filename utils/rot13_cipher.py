"""Función de cifrado ROT13."""

import codecs


def rot13_cipher(message: str) -> str:
    """
    Cifra un mensaje usando cifrado ROT13.

    Args:
        message: El mensaje de entrada a cifrar

    Returns:
        Mensaje cifrado con ROT13
    """
    return codecs.encode(message, 'rot_13')
