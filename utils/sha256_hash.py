"""Función de hashing SHA256."""

import hashlib


def sha256_hash(message: str) -> str:
    """
    Genera hash SHA256 de un mensaje.

    Args:
        message: El mensaje de entrada a hashear

    Returns:
        Hash SHA256 como cadena hexadecimal
    """
    return hashlib.sha256(message.encode()).hexdigest()
