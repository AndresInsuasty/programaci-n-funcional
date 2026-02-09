"""Base64 encoding function."""

import base64


def base64_encode(message: str) -> str:
    """
    Encode a message using Base64.
    
    Args:
        message: The input message to encode
        
    Returns:
        Base64 encoded string
    """
    return base64.b64encode(message.encode()).decode()
