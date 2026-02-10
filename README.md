# programaci-n-funcional
Repositorio de programación funcional en python, con un reto practico alineado a ciberseguridad y bigdata

## Descripción
Este proyecto implementa diferentes métodos de cifrado y hashing en Python utilizando programación funcional. Incluye 5 algoritmos diferentes que procesan mensajes de texto.

---

## 🎯 El Reto: Descifra los Mensajes

¿Alguna vez has pensado en cómo los especialistas en seguridad buscan contraseñas o mensajes cifrados? En este reto, **tú serás el hacker**.

Se te darán mensajes cifrados (en formato Base64), pero aquí viene lo interesante: **sabes exactamente cómo fueron cifrados**. Tu misión es encontrar el mensaje original de **4 caracteres** (números y letras minúsculas) usando **fuerza bruta**.

### Cómo fueron cifrados los mensajes

Cada mensaje pasó por esta cadena de transformación (en este orden):

1. **Cifrado César** (desplazamiento de 3) - Mueve cada letra 3 posiciones en el alfabeto
2. **Cifrado ROT13** - Rota cada letra 13 posiciones
3. **Hash SHA256** - Convierte el resultado en una huella digital (64 caracteres)
4. **Hash MD5** - Convierte nuevamente en otra huella digital (32 caracteres)
5. **Codificación Base64** - Convierte en texto seguro para transportar

### Ejemplos para descifrar

Aquí tienes 4 mensajes cifrados. **Tu reto es encontrar los originales:**

| Mensaje Cifrado (Base64) | Pista |
|---|---|
| `MTAyMGY5OGQ5OTdhYTdjZDRmODI1NGU2N2ZlODM2MmI=` | Comienza con una letra del inicio del alfabeto |
| `MDY5ZGFmNDQ0ZmZjOTZjNmQzN2E3YmY1Nzc4NDY4MTg=` | Una palabra común en programación |
| `ZmRjOTFkMzVlNzFiZGMxODQxMWM2Y2QzODkwNjNhNzI=` | Último recurso de un programador desesperado |
| `MGM0Mjk5ZThkOGYwMjFhNDIwZDkyNmJiYWFlZjY3ZWE=` | Lo opuesto a producción |

### ¿Cuántas combinaciones hay?

Para 4 caracteres con números (0-9) y letras minúsculas (a-z):

```
Total de combinaciones = 36^4 = 1,679,616 posibilidades
```

Parece mucho, ¿verdad? Pero no lo es tanto:

- **En una computadora moderna**: ~15-30 segundos
- **Optimizado y paralelizado**: ~1-5 segundos
- **En tu celular**: ~60-120 segundos

### 💡 La estrategia inteligente: Divide el trabajo

No necesitas resolver esto solo. **Puedes unirte con otros para dividir el trabajo**:

**Ejemplo**: Si se unen 10 personas:
- Persona 1: Busca mensajes que empiezan con letras a-c (a000...czz9)
- Persona 2: Busca mensajes que empiezan con letras d-f (d000...fzz9)
- Persona 3: Busca mensajes que empiezan con letras g-i (g000...izz9)
- ... y así sucesivamente

Cada persona solo tendría que revisar ~168,000 combinaciones en lugar de 1.6 millones. **¡10 veces más rápido!**

O más simple aún:
- Persona A: Busca con todos los números al final (ab00, ab01, ab02... ab99)
- Persona B: Busca con todo tipo de combinaciones desde su punto asignado
- Y así compartes el esfuerzo

### Recomendaciones para resolver el reto

1. **Escribe un programa en Python** que pruebe combinaciones automáticamente
2. **Optimiza tu código**: Evita crear objetos innecesarios en el bucle
3. **Usa paralelismo**: Python permite procesar múltiples candidatos en paralelo
4. **Divide con un equipo**: Acuerda quién busca en qué rango
5. **Documenta tu proceso**: Muestra cómo lo encontraste

### Hint técnico: ¿Cómo se resuelve?

Tu código debería:
```
Para cada candidato posible de 4 caracteres:
    1. Aplicar Caesar cipher (shift=3)
    2. Aplicar ROT13
    3. Aplicar SHA256
    4. Aplicar MD5
    5. Aplicar Base64
    6. Comparar con el resultado objetivo
    Si coincide → ¡Lo encontraste!
```

---

## Requisitos
- Python 3.11
- uv (gestor de paquetes)

## Instalación

1. Instalar uv (si no está instalado):
```bash
pip install uv
```

2. El proyecto ya está configurado con uv, por lo que las dependencias se instalarán automáticamente al ejecutar los comandos.

## 📁 Estructura del Proyecto

```
.
├── main.py                 # Archivo principal que orquesta todas las funciones
├── utils/                  # Carpeta con funciones de cifrado/hashing
│   ├── md5_hash.py        # Función de hash MD5
│   ├── sha256_hash.py     # Función de hash SHA256
│   ├── base64_encode.py   # Función de codificación Base64
│   ├── caesar_cipher.py   # Función de cifrado Caesar
│   └── rot13_cipher.py    # Función de cifrado ROT13
├── tests/                 # Pruebas unitarias
│   ├── test_md5_hash.py
│   ├── test_sha256_hash.py
│   ├── test_base64_encode.py
│   ├── test_caesar_cipher.py
│   └── test_rot13_cipher.py
└── README.md             # Este archivo
```

## 🚀 Cómo usar las funciones de cifrado

### Ejecutar el programa principal
```bash
uv run python main.py
```

Este demostrará todas las transformaciones con un mensaje de ejemplo.

### Ejecutar las pruebas
```bash
uv run pytest
```

### Ejecutar las pruebas con más detalle
```bash
uv run pytest -v
```

### Usar las funciones en tu propio código

Puedes importar las funciones directamente:

```python
from utils import caesar_cipher, rot13_cipher, md5_hash, sha256_hash, base64_encode

# Aplicar todas las transformaciones a un mensaje
mensaje = "ab12"
cifrado1 = caesar_cipher(mensaje, shift=3)
cifrado2 = rot13_cipher(cifrado1)
hash1 = sha256_hash(cifrado2)
hash2 = md5_hash(hash1)
resultado_final = base64_encode(hash2)

print(resultado_final)  # Resultado en Base64
```

## 🔐 Algoritmos Implementados

Cada función está completamente documentada y lista para usar:

### 1️⃣ Caesar Cipher
- **Qué hace**: Desplaza cada letra del alfabeto una cantidad fija de posiciones
- **Este proyecto**: Usa desplazamiento de 3
- **Ejemplo**: "abc" → "def"
- **¿Se puede revertir?**: Sí, es reversible

### 2️⃣ ROT13 Cipher
- **Qué hace**: Especial tipo de Caesar que rota 13 posiciones exactas
- **Ejemplo**: "abc" → "nop"
- **¿Se puede revertir?**: Sí, es totalmente reversible (ROT13 dos veces = original)

### 3️⃣ SHA256 Hash
- **Qué hace**: Convierte cualquier texto en una "huella digital" de 64 caracteres
- **Ejemplo**: "test" → `75f9e16ad373a52a4cca45022d192f6f9d719a34847e8c9d11c897e3aafd8dad`
- **¿Se puede revertir?**: **NO**, es irreversible
- **Uso**: Proteger contraseñas

### 4️⃣ MD5 Hash
- **Qué hace**: Similar a SHA256, crea una huella digital de 32 caracteres
- **¿Se puede revertir?**: **NO**, es irreversible
- **Nota**: MD5 es más antigua, pero sirve para este ejercicio

### 5️⃣ Base64 Encoding
- **Qué hace**: Convierte datos binarios en texto legible y seguro
- **Ejemplo**: "test" → `dGVzdA==`
- **¿Se puede revertir?**: Sí, es completamente reversible
- **Uso**: Transportar datos por internet sin problemas

## 📊 Ejemplo de Salida

Cuando ejecutas `uv run python main.py`, verás esto:

```
================================================================================
DEMOSTRACIÓN DE CIFRADO Y HASHING
================================================================================

Mensaje original: Hello, World! This is a test message for encryption.

--------------------------------------------------------------------------------

1. MD5 Hash:
   9cf1b30cbcc693e8df71483bdb7e72a6

2. SHA256 Hash:
   73a157f66c7a2c0df98badcc482b92be50b1fee8f82122cc8873f1d1758651f1

3. Codificación Base64:
   SGVsbG8sIFdvcmxkISBUaGlzIGlzIGEgdGVzdCBtZXNzYWdlIGZvciBlbmNyeXB0aW9uLg==

4. Cifrado César (desplazamiento=3):
   Khoor, Zruog! Wklv lv d whvw phvvdjh iru hqfubswlrq.

5. Cifrado ROT13:
   Uryyb, Jbeyq! Guvf vf n grfg zrffntr sbe rapelcgvba.

================================================================================
¡Todos los métodos de cifrado y hashing completados exitosamente!
================================================================================
```

## ✅ Tests

El proyecto incluye 35 pruebas unitarias que cubren todos los algoritmos implementados:
- 6 tests para MD5
- 6 tests para SHA256
- 6 tests para Base64
- 6 tests para Caesar Cipher
- 6 tests para ROT13 Cipher

Estas pruebas garantizan que todas las funciones funcionen correctamente.

---

## 📝 Notas finales

- Este proyecto es educativo y demuestra los conceptos básicos de criptografía
- Los algoritmos aquí son conocidos públicamente, no inventes uno propio para seguridad real
- Para seguridad real, siempre usa librerías criptográficas confiables
