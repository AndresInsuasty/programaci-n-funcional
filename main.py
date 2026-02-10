"""Módulo principal para orquestar funciones de cifrado y hashing."""

from utils import (
    md5_hash,
    sha256_hash,
    base64_encode,
    caesar_cipher,
    rot13_cipher,
)


def main():
    """Función principal para orquestar todos los métodos de cifrado y hashing."""
    # Generar un mensaje
    message = "Hello, World! This is a test message for encryption."
    
    print("=" * 80)
    print("DEMOSTRACIÓN DE CIFRADO Y HASHING")
    print("=" * 80)
    print(f"\nMensaje original: {message}")
    print("\n" + "-" * 80)

    # Aplicar hash MD5
    md5_result = md5_hash(message)
    print(f"\n1. MD5 Hash:")
    print(f"   {md5_result}")

    # Aplicar hash SHA256
    sha256_result = sha256_hash(message)
    print(f"\n2. SHA256 Hash:")
    print(f"   {sha256_result}")

    # Aplicar codificación Base64
    base64_result = base64_encode(message)
    print(f"\n3. Codificación Base64:")
    print(f"   {base64_result}")

    # Aplicar cifrado César con desplazamiento de 3
    caesar_result = caesar_cipher(message, shift=3)
    print(f"\n4. Cifrado César (desplazamiento=3):")
    print(f"   {caesar_result}")

    # Aplicar cifrado ROT13
    rot13_result = rot13_cipher(message)
    print(f"\n5. Cifrado ROT13:")
    print(f"   {rot13_result}")
    
    print("\n" + "=" * 80)
    print("Todos los métodos de cifrado y hashing completados exitosamente!")
    print("=" * 80)


if __name__ == "__main__":
    main()
