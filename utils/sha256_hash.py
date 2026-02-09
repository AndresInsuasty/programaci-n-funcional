"""SHA256 hashing function."""

import hashlib


def sha256_hash(message: str) -> str:
    """
    Generate SHA256 hash of a message.
    
    Args:
        message: The input message to hash
        
    Returns:
        SHA256 hash as hexadecimal string
    """
    return hashlib.sha256(message.encode()).hexdigest()
