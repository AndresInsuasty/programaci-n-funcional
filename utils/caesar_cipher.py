"""Caesar cipher encryption function."""


def caesar_cipher(message: str, shift: int = 3) -> str:
    """
    Encrypt a message using Caesar cipher.
    
    Args:
        message: The input message to encrypt
        shift: Number of positions to shift (default: 3)
        
    Returns:
        Encrypted message
    """
    result = []
    for char in message:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            shifted = (ord(char) - ascii_offset + shift) % 26
            result.append(chr(shifted + ascii_offset))
        else:
            # Keep non-alphabetic characters as is
            result.append(char)
    return ''.join(result)
