"""Función de cifrado César."""


def caesar_cipher(message: str, shift: int = 3) -> str:
    """
    Cifra un mensaje usando el cifrado César.

    Args:
        message: El mensaje de entrada a cifrar
        shift: Número de posiciones a desplazar (por defecto: 3)

    Returns:
        Mensaje cifrado
    """
    result = []
    for char in message:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Desplazar carácter y envolver alrededor del alfabeto
            shifted = (ord(char) - ascii_offset + shift) % 26
            result.append(chr(shifted + ascii_offset))
        else:
            # Mantener caracteres no alfabéticos tal como están
            result.append(char)
    return ''.join(result)
