"""Función de codificación Base64."""

import base64


def base64_encode(message: str) -> str:
    """
    Codifica un mensaje usando Base64.

    Args:
        message: El mensaje de entrada a codificar

    Returns:
        Cadena codificada en Base64
    """
    return base64.b64encode(message.encode()).decode()
