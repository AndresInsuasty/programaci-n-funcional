# programaci-n-funcional
Repositorio de programación funcional en python, con un reto practico alineado a ciberseguridad y bigdata

## Descripción
Este proyecto implementa diferentes métodos de cifrado y hashing en Python utilizando programación funcional. Incluye 5 algoritmos diferentes que procesan mensajes de texto.

## Requisitos
- Python 3.11
- uv (gestor de paquetes)

## Instalación

1. Instalar uv (si no está instalado):
```bash
pip install uv
```

2. El proyecto ya está configurado con uv, por lo que las dependencias se instalarán automáticamente al ejecutar los comandos.

## Estructura del Proyecto

```
.
├── main.py                 # Archivo principal que orquesta todas las funciones
├── utils/                  # Carpeta con funciones de cifrado/hashing
│   ├── md5_hash.py        # Función de hash MD5
│   ├── sha256_hash.py     # Función de hash SHA256
│   ├── base64_encode.py   # Función de codificación Base64
│   ├── caesar_cipher.py   # Función de cifrado Caesar
│   └── rot13_cipher.py    # Función de cifrado ROT13
└── tests/                 # Pruebas unitarias
    ├── test_md5_hash.py
    ├── test_sha256_hash.py
    ├── test_base64_encode.py
    ├── test_caesar_cipher.py
    └── test_rot13_cipher.py
```

## Uso

### Ejecutar el programa principal
```bash
uv run python main.py
```

### Ejecutar las pruebas
```bash
uv run pytest
```

### Ejecutar las pruebas con más detalle
```bash
uv run pytest -v
```

## Algoritmos Implementados

1. **MD5 Hash**: Genera un hash MD5 del mensaje (32 caracteres hexadecimales)
2. **SHA256 Hash**: Genera un hash SHA256 del mensaje (64 caracteres hexadecimales)
3. **Base64 Encoding**: Codifica el mensaje en Base64
4. **Caesar Cipher**: Cifrado por sustitución con desplazamiento de 3 posiciones
5. **ROT13 Cipher**: Cifrado por sustitución con desplazamiento de 13 posiciones

## Ejemplo de Salida

```
================================================================================
ENCRYPTION AND HASHING DEMO
================================================================================

Original message: Hello, World! This is a test message for encryption.

--------------------------------------------------------------------------------

1. MD5 Hash:
   9cf1b30cbcc693e8df71483bdb7e72a6

2. SHA256 Hash:
   73a157f66c7a2c0df98badcc482b92be50b1fee8f82122cc8873f1d1758651f1

3. Base64 Encoding:
   SGVsbG8sIFdvcmxkISBUaGlzIGlzIGEgdGVzdCBtZXNzYWdlIGZvciBlbmNyeXB0aW9uLg==

4. Caesar Cipher (shift=3):
   Khoor, Zruog! Wklv lv d whvw phvvdjh iru hqfubswlrq.

5. ROT13 Cipher:
   Uryyb, Jbeyq! Guvf vf n grfg zrffntr sbe rapelcgvba.

================================================================================
All encryption and hashing methods completed successfully!
================================================================================
```

## Tests

El proyecto incluye 35 pruebas unitarias que cubren todos los algoritmos implementados:
- 6 tests para MD5
- 6 tests para SHA256
- 6 tests para Base64
- 9 tests para Caesar Cipher
- 8 tests para ROT13

Todas las pruebas validan diferentes casos de uso, incluyendo:
- Cadenas vacías
- Números
- Caracteres especiales
- Unicode
- Consistencia de resultados
