"""MD5 hashing function."""

import hashlib


def md5_hash(message: str) -> str:
    """
    Generate MD5 hash of a message.
    
    Args:
        message: The input message to hash
        
    Returns:
        MD5 hash as hexadecimal string
    """
    return hashlib.md5(message.encode()).hexdigest()
