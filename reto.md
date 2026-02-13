# 🎯 Reto Avanzado: Descifrar Mensajes de 5 Caracteres

Este es un reto avanzado de fuerza bruta para descifrar mensajes de **5 caracteres** que fueron procesados a través del pipeline completo de transformaciones.

## 📋 Características del Reto

### Parámetros del Mensaje Original
- **Longitud**: Exactamente 5 caracteres
- **Caracteres permitidos**: Solo letras minúsculas (a-z)
- **Total**: 26 caracteres posibles por posición

### Espacio de Búsqueda
```
Total de combinaciones = 26^5 = 11,881,376 (11.88 millones)
```

⚠️ **Nivel de dificultad**: Este reto es 7,076 veces más difícil que el reto básico de 4 caracteres (con 36 caracteres).

### Factibilidad Técnica

**Tiempo de cálculo (fuerza bruta completa):**
- CPU moderna (single-core, ~60k intentos/seg): **~3.3 minutos**
- CPU 8 núcleos: **~30-45 segundos**
- Computacionalmente factible ✅

**Almacenamiento (rainbow table completa):**
- 11,881,376 combinaciones × ~56 bytes/entrada = **~665 MB**
- Cabe en cualquier computadora moderna ✅
- Perfecto para proyecto educativo de rainbow tables

### Pipeline de Transformación

Los mensajes fueron procesados en este orden:

1. **Caesar Cipher** (desplazamiento = 3)
2. **ROT13**
3. **SHA256 Hash**
4. **MD5 Hash**
5. **Base64 Encoding**

## 🔐 Lista de Mensajes Cifrados

Aquí están los 20 mensajes para descifrar. Cada uno tiene una pista que puede ayudarte a reducir el espacio de búsqueda.

| # | Hash (Base64) | Pista | Longitud |
|---|---|---|---|
| 1 | `ODllNjNiNGVhNDVmYmQxNTgzNGM2YmJiMzQ2ZTUyMWU=` | Lenguaje de serpientes | 6 caracteres |
| 2 | `MTMxNzRkN2RkMGFmMGRhZDQxMjQ3MmI2Y2MwYWM0YmQ=` | Sistema operativo libre | 5 caracteres |
| 3 | `Nzc3ZjZjZDg2NWEwZDM3MzkzNWI3MDMxYTNhZGRiNWQ=` | Base de datos relacional | 5 caracteres |
| 4 | `MTZlYzM1NTJiYTE0MTFmZjgwZTYwOGY1YTQwNDY2NGY=` | Base de datos en memoria | 5 caracteres |
| 5 | `YWVjMzkwYjk0ZjkxODk2YmI4NzIyYTdmZGQ1ZWZmZjc=` | Servidor web y proxy | 5 caracteres |
| 6 | `ZjllOTJkOWM4YjMyYmViZDRkMjc1Mjc5NjNlNTVhYTI=` | Microframework web Python | 5 caracteres |
| 7 | `M2JmM2I0NjdkYmU4Yjk3YzlkNDFlMTQ3NTE5Mjg4YTg=` | Librería de interfaces | 5 caracteres |
| 8 | `NWJjMWI4YTA2YWIwZTQ5ODE1NzRmMTg0ODRkZTU3ZTg=` | Sistema de mensajería | 5 caracteres |
| 9 | `ODNhMTg4YmYxMmMwZjJiMzg4YTFmNDI0MmM3ODRmN2Q=` | Base de datos NoSQL | 5 caracteres |
| 10 | `NTNkY2QxZWI3YThjOWZhMzBlNmQ4NjFmZGMwY2M4YmY=` | Plataforma de contenedores | 6 caracteres |
| 11 | `ZGZiM2U4NTMzMjliOGUxZjZhM2U3YmQyMzJhNjQyNTk=` | Intérprete de comandos | 5 caracteres |
| 12 | `MGIyYTQzYTE4MjNjYTMyN2UzNDkxOTA3Njk1NGNjODM=` | Protocolo seguro web | 5 caracteres |
| 13 | `NTA4M2QzOGNkZDk2M2FjMGFiZDAxZTJhZTJhOGJiMTY=` | Usuario con privilegios | 5 caracteres |
| 14 | `NzRhNzliNjJiYmM3ODZhMmUxMTU2NDNkOTNkNjc5Yjg=` | Inicio de sesión | 5 caracteres |
| 15 | `NzBiZmY2Yjk4YzdhZDE4YzE1NGZhNmRlYmQ5MmJiOTg=` | Credencial de acceso | 5 caracteres |
| 16 | `MjZiYjkxMmYzZWQ1OTQxYzJhMzkxYjY3Njg3YjU3YWY=` | Almacenamiento temporal | 5 caracteres |
| 17 | `MDQ1YmU0NzQzNGQ4NDFjOWVjOWI1YTI5ODI2NjgyYzk=` | Consulta a base de datos | 5 caracteres |
| 18 | `OGZmOTY0NDg1ODJmNmEwZTQwMWI4MjM0ZjAyZjFjMDA=` | Búsqueda de errores | 5 caracteres |
| 19 | `NmI2Yzc3ZDVkODFmNWQ2MDVkY2FmMzEwYzUzZmI2N2M=` | Ejecución asíncrona | 5 caracteres |
| 20 | `MWEwNDA0ZjllOTFmMmNiMzA1YWY0MzQ4OWYzNjRhM2I=` | Fallo en el sistema | 5 caracteres |

## 💡 Estrategias Recomendadas

### 1. Usar las Pistas (Recomendado)
Las pistas te dan información sobre el mensaje original. Por ejemplo:
- "Lenguaje de serpientes" → **python**
- "Sistema operativo libre" → **linux**
- "Base de datos relacional" → **mysql**

### 2. Búsqueda Basada en Diccionario
En lugar de fuerza bruta completa, crea una lista de palabras candidatas relacionadas con la pista:

```python
# Ejemplo para el mensaje #2 (Sistema operativo libre)
candidatos = ["linux", "unix", "fedora", "debian", "ubuntu"]

for candidato in candidatos:
    if len(candidato) == 5:  # Solo 5 caracteres
        resultado = aplicar_pipeline_completo(candidato)
        if resultado == objetivo:
            print(f"¡Encontrado! {candidato}")
```

### 3. Fuerza Bruta Completa (Factible)
A diferencia del reto anterior de 6 caracteres, **este SÍ es factible resolver por fuerza bruta completa** en pocos minutos:

```python
import string
import itertools

caracteres = string.ascii_lowercase  # Solo a-z
for combinacion in itertools.product(caracteres, repeat=5):
    candidato = ''.join(combinacion)
    # Aplicar pipeline y comparar
```

### 4. Proyecto de Rainbow Table
Este reto es **perfecto para crear una rainbow table completa**:
- Solo necesitas ~665 MB de almacenamiento
- Puedes calcularla en minutos
- Una vez generada, la búsqueda es instantánea

## 🚀 Cómo Ejecutar

### Opción 1: Modificar solucion.py para 5 caracteres

```python
# Cambiar en generar_candidatos():
caracteres = string.ascii_lowercase  # Solo letras minúsculas

# Cambiar la longitud:
for combinacion in itertools.product(caracteres, repeat=5):  # 5 en lugar de 4
```

### Opción 2: Usar Diccionario Inteligente

```python
# Lista de palabras comunes en tecnología de 5 letras
palabras = [
    "aaaaa", "bbbbbb", "ccccc", "ddddd", "eeeee", "fffff", "ggggg", "hhhhh", "iiiii",
]

for palabra in palabras:
    resultado = aplicar_pipeline_completo(palabra)
    if resultado == hash_objetivo:
        print(f"¡Encontrado! {palabra}")
```

## ⏱️ Estimación de Tiempo

| Estrategia | Tiempo Estimado |
|------------|-----------------|
| Búsqueda con diccionario inteligente | Segundos |
| Fuerza bruta completa (1 núcleo) | ~3.3 minutos |
| Fuerza bruta completa (8 núcleos) | ~30-45 segundos |
| Consulta a rainbow table precalculada | Milisegundos |

## 🗄️ Proyecto Bonus: Crear Tu Propia Rainbow Table

Este reto es ideal para crear una rainbow table completa como proyecto educativo:

```python
import sqlite3
import string
import itertools

def crear_rainbow_table(output_db="rainbow_5chars.db"):
    """Genera una rainbow table completa de 5 caracteres."""
    conn = sqlite3.connect(output_db)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS rainbow
                 (mensaje TEXT PRIMARY KEY, hash TEXT NOT NULL)''')
    c.execute('CREATE INDEX IF NOT EXISTS idx_hash ON rainbow(hash)')

    caracteres = string.ascii_lowercase
    total = 26 ** 5
    batch = []

    print(f"Generando {total:,} combinaciones...")

    for i, combo in enumerate(itertools.product(caracteres, repeat=5)):
        mensaje = ''.join(combo)
        hash_resultado = aplicar_pipeline_completo(mensaje)
        batch.append((mensaje, hash_resultado))

        if len(batch) >= 10000:
            c.executemany('INSERT OR IGNORE INTO rainbow VALUES (?,?)', batch)
            conn.commit()
            batch = []

            if i % 100000 == 0:
                print(f"Progreso: {i:,}/{total:,} ({i/total*100:.2f}%)")

    if batch:
        c.executemany('INSERT OR IGNORE INTO rainbow VALUES (?,?)', batch)
        conn.commit()

    conn.close()
    print(f"¡Rainbow table completada! Tamaño: ~665 MB")

# Usar la rainbow table
def buscar_en_rainbow(hash_objetivo, db_path="rainbow_5chars.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT mensaje FROM rainbow WHERE hash = ?', (hash_objetivo,))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None
```

**Ventajas de este enfoque:**
- ✅ Generas la tabla una sola vez (~3 minutos)
- ✅ Búsqueda instantánea para cualquier hash
- ✅ Solo ~665 MB de almacenamiento

## 🏆 Desafío Extra

Una vez que descifres los 20 mensajes, intenta:

1. **Crear tu propia rainbow table completa** y comparte el tiempo que tardó
2. **Medir la diferencia de velocidad** entre fuerza bruta y rainbow table
3. **Comparar diferentes estrategias**: diccionario vs fuerza bruta vs rainbow table
4. **Generar tus propios mensajes cifrados** y desafiar a tus compañeros

---

**Suerte con el reto** 🚀 