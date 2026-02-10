"""Función de hashing MD5."""

import hashlib


def md5_hash(message: str) -> str:
    """
    Genera hash MD5 de un mensaje.

    Args:
        message: El mensaje de entrada a hashear

    Returns:
        Hash MD5 como cadena hexadecimal
    """
    return hashlib.md5(message.encode()).hexdigest()
