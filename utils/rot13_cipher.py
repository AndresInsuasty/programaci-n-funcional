"""ROT13 cipher encryption function."""

import codecs


def rot13_cipher(message: str) -> str:
    """
    Encrypt a message using ROT13 cipher.
    
    Args:
        message: The input message to encrypt
        
    Returns:
        ROT13 encrypted message
    """
    return codecs.encode(message, 'rot_13')
