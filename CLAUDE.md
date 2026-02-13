# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Descripción del Proyecto

Este es un proyecto educativo de programación funcional en Python enfocado en criptografía básica y seguridad informática. El proyecto implementa 5 algoritmos de cifrado/hashing (Caesar cipher, ROT13, SHA256, MD5, Base64) y presenta un reto práctico de fuerza bruta para descifrar mensajes de 4 caracteres.

**Idioma**: Este proyecto está completamente documentado en español. Todo el código, comentarios, docstrings, mensajes de commit y documentación deben estar en español.

## Comandos Comunes

### Desarrollo
```bash
# Ejecutar el programa principal (demo de todos los algoritmos)
uv run python main.py

# Ejecutar todas las pruebas
uv run pytest

# Ejecutar pruebas con output detallado
uv run pytest -v

# Ejecutar una sola prueba específica
uv run pytest tests/test_caesar_cipher.py

# Ejecutar linting con pylint
uv run pylint utils/ tests/ main.py
```

### Solución del Reto (Fuerza Bruta)
```bash
# Ejecutar con el hash por defecto del código
uv run python solucion.py

# Ejecutar con un hash personalizado
uv run python solucion.py "MTAyMGY5OGQ5OTdhYTdjZDRmODI1NGU2N2ZlODM2MmI="

# El script mostrará:
# - Progreso cada 10,000 intentos
# - Tiempo transcurrido en tiempo real
# - Velocidad de procesamiento (intentos/segundo)
# - Tiempo total de búsqueda y ejecución
```

### Gestión de Dependencias
```bash
# Instalar uv (si no está instalado)
pip install uv

# Las dependencias se instalan automáticamente al ejecutar comandos con uv
# No se requiere instalación manual de dependencias
```

## Arquitectura del Código

### Enfoque de Programación Funcional

Este proyecto sigue principios de **programación funcional pura**:

- **Funciones puras**: Todas las funciones en `utils/` son puras - dado el mismo input, siempre devuelven el mismo output sin efectos secundarios
- **Inmutabilidad**: Las funciones no modifican sus argumentos; devuelven nuevos valores
- **Sin estado compartido**: Cada función opera de forma independiente
- **Composición**: Las funciones están diseñadas para ser componibles - la salida de una función puede ser la entrada de otra

### Estructura Modular

```
utils/
├── caesar_cipher.py   # Cifrado Caesar (desplazamiento alfabético)
├── rot13_cipher.py    # Cifrado ROT13 (desplazamiento fijo de 13)
├── sha256_hash.py     # Hash SHA256 (irreversible)
├── md5_hash.py        # Hash MD5 (irreversible)
└── base64_encode.py   # Codificación Base64 (reversible)
```

Cada módulo exporta **una sola función principal** con el mismo nombre que el archivo. Todas las funciones siguen el patrón:

```python
def nombre_funcion(input: str, **kwargs) -> str:
    """Docstring en español."""
    # Implementación funcional pura
    return resultado
```

### Pipeline de Transformación del Reto

El reto principal requiere aplicar las funciones en este orden específico:

1. **Caesar cipher** (shift=3) → cifra el texto
2. **ROT13** → cifra el resultado anterior
3. **SHA256** → genera hash del texto cifrado
4. **MD5** → genera hash del hash anterior
5. **Base64** → codifica el hash MD5 final

Esta secuencia es la que se debe **revertir** (donde sea posible) o **replicar por fuerza bruta** para resolver el reto de descifrado.

### Sistema de Tests

Cada algoritmo tiene su propio archivo de tests con ~6-9 casos de prueba que cubren:
- Caso básico (comportamiento por defecto)
- Casos edge (valores límite, wrap-around)
- Preservación de caracteres especiales
- Manejo de mayúsculas/minúsculas
- Casos de error o inválidos

Los tests están diseñados para ejecutarse de forma independiente y en cualquier orden.

## Convenciones del Proyecto

### Estilo de Código
- **Docstrings**: Todas las funciones deben tener docstrings en español con formato Google style
- **Type hints**: Usar type hints en todas las firmas de funciones
- **Nombres**: snake_case para funciones y variables, en español cuando sea posible
- **Línea máxima**: 88 caracteres (compatible con Black)

### Tests
- Nombrar funciones de test como `test_<funcion>_<caso_especifico>`
- Cada test debe probar un solo aspecto del comportamiento
- Usar mensajes descriptivos en español para los docstrings de los tests
- Preferir asserts simples sobre frameworks complejos

### Imports
El archivo `utils/__init__.py` centraliza todos los exports. Siempre importar desde `utils`:
```python
from utils import caesar_cipher, rot13_cipher, sha256_hash
```

No importar directamente de submódulos:
```python
# ❌ Evitar
from utils.caesar_cipher import caesar_cipher

# ✅ Preferir
from utils import caesar_cipher
```

## Notas Importantes

### Seguridad
- Este es un proyecto **educativo únicamente**
- Los algoritmos MD5 y Caesar/ROT13 **no son seguros** para uso real
- El propósito es demostrar conceptos de criptografía y programación funcional
- Para aplicaciones reales, usar librerías criptográficas establecidas

### Contexto del Reto

#### Reto Básico (README.md)
- Los mensajes objetivo son de exactamente **4 caracteres** (a-z, 0-9)
- Total de combinaciones posibles: 36^4 = 1,679,616
- El reto está diseñado para ser resuelto mediante **fuerza bruta paralelizada**
- Se espera que los estudiantes trabajen en equipo dividiendo el espacio de búsqueda

#### Reto Avanzado (reto.md)
- Los mensajes objetivo son de exactamente **5 caracteres** (solo letras minúsculas a-z)
- Total de combinaciones posibles: 26^5 = 11,881,376 (11.88 millones)
- **SÍ es práctico resolverlo por fuerza bruta** (~3 minutos en 1 núcleo, ~30 segundos en 8 núcleos)
- **Rainbow table completa es factible**: ~665 MB de almacenamiento, ~3 minutos de generación
- Perfecto para proyectos educativos de rainbow tables
- Las pistas permiten estrategias de diccionario inteligente (solución en segundos)
- Ejemplo: "Lenguaje de serpientes" → candidatos como "python", "snake", etc.
