"""Main module to orchestrate encryption and hashing functions."""

from utils import (
    md5_hash,
    sha256_hash,
    base64_encode,
    caesar_cipher,
    rot13_cipher,
)


def main():
    """Main function to orchestrate all encryption and hashing methods."""
    # Generate a message
    message = "Hello, World! This is a test message for encryption."
    
    print("=" * 80)
    print("ENCRYPTION AND HASHING DEMO")
    print("=" * 80)
    print(f"\nOriginal message: {message}")
    print("\n" + "-" * 80)
    
    # Apply MD5 hash
    md5_result = md5_hash(message)
    print(f"\n1. MD5 Hash:")
    print(f"   {md5_result}")
    
    # Apply SHA256 hash
    sha256_result = sha256_hash(message)
    print(f"\n2. SHA256 Hash:")
    print(f"   {sha256_result}")
    
    # Apply Base64 encoding
    base64_result = base64_encode(message)
    print(f"\n3. Base64 Encoding:")
    print(f"   {base64_result}")
    
    # Apply Caesar cipher with shift of 3
    caesar_result = caesar_cipher(message, shift=3)
    print(f"\n4. Caesar Cipher (shift=3):")
    print(f"   {caesar_result}")
    
    # Apply ROT13 cipher
    rot13_result = rot13_cipher(message)
    print(f"\n5. ROT13 Cipher:")
    print(f"   {rot13_result}")
    
    print("\n" + "=" * 80)
    print("All encryption and hashing methods completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
