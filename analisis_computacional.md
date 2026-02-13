# 🖥️ Análisis Computacional: Rainbow Table Completa

Este documento analiza el costo computacional y de almacenamiento para generar y guardar **todas las combinaciones posibles** del reto avanzado (5 caracteres, solo letras minúsculas).

## 📊 Parámetros del Problema

### Espacio de Búsqueda
```
Caracteres: a-z = 26 caracteres (solo letras minúsculas)
Longitud: 5 caracteres
Total combinaciones: 26^5 = 11,881,376
```

**11.88 millones de combinaciones** - Perfectamente manejable ✅

### Pipeline por Mensaje
Para cada mensaje debemos calcular:
1. Caesar cipher (shift=3)
2. ROT13
3. SHA256 hash
4. MD5 hash
5. Base64 encoding

## ⏱️ Estimación de Tiempo

### Benchmark en Hardware Moderno

Basándonos en pruebas con el script `solucion.py`:

**CPU moderna (single-core):**
- Velocidad típica: **50,000 - 80,000 intentos/segundo**
- Promedio conservador: **60,000 intentos/segundo**

### Cálculo de Tiempo (Sin Paralelización)

```
Total combinaciones: 11,881,376
Velocidad: 60,000 intentos/seg

Tiempo = 11,881,376 / 60,000
      = 198 segundos
      = 3.3 minutos
```

**⏰ Tiempo estimado: ~3.3 minutos** (sin paralelización)

### Cálculo con Paralelización

Con CPU de **8 núcleos** (eficiencia ~75% debido a overhead):

```
Speedup efectivo: 8 × 0.75 = 6x
Tiempo = 3.3 minutos / 6 = 0.55 minutos = ~33 segundos
```

**⏰ Tiempo estimado: ~30-45 segundos** (8 núcleos)

Con CPU de **16 núcleos**:

```
Speedup efectivo: 16 × 0.70 = 11.2x
Tiempo = 3.3 minutos / 11.2 = 0.29 minutos = ~18 segundos
```

**⏰ Tiempo estimado: ~15-20 segundos** (16 núcleos)

### Hardware Especializado

Con **GPU (CUDA)** optimizado para hashing:
- Velocidad: ~10-50 millones intentos/segundo
- Tiempo: **Menos de 1 segundo** ⚡

Con **cluster distribuido** (100 máquinas de 8 núcleos):
- Tiempo: **Menos de 1 segundo** (overkill para este reto)

## 💾 Almacenamiento Requerido

### Tamaño por Entrada

Cada entrada en la rainbow table contendría:

```
- Mensaje original: 6 bytes (6 caracteres ASCII)
- Hash Base64: 45 bytes (resultado final)
- Separador/formato: 5 bytes
- Total por entrada: ~56 bytes
```

### Tamaño Total

```
11,881,376 combinaciones × 56 bytes = 665,357,056 bytes
                                     = 665 MB
                                     = 0.665 GB
```

**💽 Almacenamiento necesario: ~665 MB** ✅

### Formato de Almacenamiento

#### Opción 1: Archivo de Texto Plano
```
mensaje,hash_base64
aaaaa,YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=
aaaab,YjJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXo=
...
```
- Tamaño: ~665 MB
- Velocidad de búsqueda: Lenta (búsqueda lineal)

#### Opción 2: Base de Datos SQLite (Recomendado)
```sql
CREATE TABLE rainbow (
    mensaje TEXT PRIMARY KEY,
    hash TEXT NOT NULL
);
CREATE INDEX idx_hash ON rainbow(hash);
```
- Tamaño: ~750 MB (con índices)
- Velocidad de búsqueda: Rápida (búsqueda indexada, milisegundos)
- Ideal para este proyecto

#### Opción 3: Base de Datos en Memoria (Redis)
- Tamaño RAM necesaria: ~800 MB
- Velocidad de búsqueda: Muy rápida (O(1), microsegundos)
- Perfectamente factible en cualquier computadora moderna

## 💰 Costo Económico

### Hardware Propio

**CPU moderna (cualquier laptop/desktop):**
- Costo computacional: ~$0.01 USD (electricidad, 3 minutos @ $0.12/kWh)
- Disco: Ya tienes espacio suficiente (solo 665 MB)
- **Total: Prácticamente gratis** ✅

### Cloud Computing (AWS/GCP/Azure)

**Opción 1: Computación bajo demanda**
```
Instancia t3.medium (2 vCPUs) - suficiente
- Costo: $0.0416/hora
- Tiempo: 0.05 horas (3 minutos)
- Total: ~$0.002 USD (menos de 1 centavo)
```

**Almacenamiento S3/Cloud Storage:**
```
0.665 GB @ $0.023/GB/mes = $0.015/mes (1.5 centavos)
```

**💵 Costo total en cloud: < $0.01 USD** (ridículamente barato)

## 📈 Comparación con el Reto Básico

| Característica | Reto Básico (4 chars, 36 chars) | Reto Avanzado (5 chars, 26 chars) |
|---|---|---|
| Combinaciones | 1,679,616 | 11,881,376 |
| Factor | 1x | **7.1x más** |
| Tiempo (CPU 8 núcleos) | ~30 segundos | ~30-45 segundos |
| Almacenamiento | ~90 MB | ~665 MB |
| Factibilidad | ✅ Trivial | ✅ Muy factible |

## 🎯 Conclusiones Educativas

### Para Estudiantes

1. **Factibilidad Técnica** ✅:
   - TOTALMENTE factible generar la rainbow table completa
   - Solo requiere ~3 minutos con hardware moderno
   - Necesita solo ~665 MB de almacenamiento (¡cabe en un USB!)

2. **Factibilidad Económica** 💰:
   - Costo: Prácticamente gratis (menos de 1 centavo)
   - Tiempo de inversión: Minutos, no días
   - **Perfecto para proyecto individual o de equipo**

3. **Lecciones Aprendidas** 📚:
   - Las rainbow tables son **muy prácticas para espacios pequeños**
   - Demuestran por qué los passwords deben ser largos (8+ caracteres)
   - Explican por qué el "salt" es crucial en hashing de contraseñas
   - Introducen el concepto de trade-offs: espacio vs. tiempo de cálculo

### ¿Por Qué las Contraseñas Reales Son Seguras?

Si extendemos el análisis a contraseñas reales de **8 caracteres** con caracteres especiales (~95 caracteres):

```
95^8 = 6,634,204,312,890,625 combinaciones
     = 6.6 cuatrillones

Tiempo (CPU 8 núcleos): ~3,500 años
Almacenamiento: ~360 PB (petabytes)
Costo almacenamiento: ~$8 millones USD/mes
```

**¡Computacionalmente inviable!** 🚫

Por eso las contraseñas modernas usan:
- **Salt**: Valores aleatorios únicos por usuario que invalidan rainbow tables precalculadas
- **Key stretching**: Algoritmos como bcrypt, scrypt, Argon2 que son intencionalmente lentos
- **Longitud mínima**: 8-12+ caracteres con múltiples tipos

## 🔬 Proyecto RECOMENDADO para Estudiantes

### Desafío: Generar Rainbow Table Completa del Reto

Genera la rainbow table completa de 5 caracteres (solo letras minúsculas):
- **Espacio completo**: 26^5 = 11.88 millones de combinaciones
- **Tiempo estimado**: ~3 minutos (single-core), ~30 segundos (8 núcleos)
- **Almacenamiento**: ~665 MB (cabe en cualquier USB moderno)
- **Perfectamente factible** como proyecto estudiantil ✅

### Código Base

```python
import string
import itertools
import sqlite3
import time
from utils import caesar_cipher, rot13_cipher, sha256_hash, md5_hash, base64_encode

def aplicar_pipeline_completo(mensaje: str) -> str:
    """Aplica el pipeline completo de transformaciones."""
    paso1 = caesar_cipher(mensaje, shift=3)
    paso2 = rot13_cipher(paso1)
    paso3 = sha256_hash(paso2)
    paso4 = md5_hash(paso3)
    paso5 = base64_encode(paso4)
    return paso5

def generar_rainbow_table(output_db="rainbow_5chars.db"):
    """Genera una rainbow table completa de 5 caracteres (solo a-z)."""
    print("Iniciando generación de rainbow table...")
    print("Parámetros: 5 caracteres, solo letras minúsculas (a-z)")
    print(f"Total de combinaciones: {26**5:,}\n")

    inicio = time.time()

    conn = sqlite3.connect(output_db)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS rainbow
                 (mensaje TEXT PRIMARY KEY, hash TEXT NOT NULL)''')
    c.execute('CREATE INDEX IF NOT EXISTS idx_hash ON rainbow(hash)')

    caracteres = string.ascii_lowercase  # Solo a-z
    total = 26 ** 5

    batch = []
    for i, combinacion in enumerate(itertools.product(caracteres, repeat=5)):
        mensaje = ''.join(combinacion)
        hash_resultado = aplicar_pipeline_completo(mensaje)
        batch.append((mensaje, hash_resultado))

        # Insertar por lotes cada 10,000 entradas
        if len(batch) >= 10000:
            c.executemany('INSERT OR IGNORE INTO rainbow VALUES (?,?)', batch)
            conn.commit()
            batch = []

            if (i + 1) % 100000 == 0:
                transcurrido = time.time() - inicio
                progreso = (i + 1) / total * 100
                velocidad = (i + 1) / transcurrido
                estimado = (total - i - 1) / velocidad
                print(f"Progreso: {i+1:,}/{total:,} ({progreso:.2f}%) | "
                      f"Velocidad: {velocidad:,.0f} combinaciones/seg | "
                      f"Tiempo restante: {estimado:.0f}s")

    # Insertar cualquier entrada restante
    if batch:
        c.executemany('INSERT OR IGNORE INTO rainbow VALUES (?,?)', batch)
        conn.commit()

    conn.close()

    tiempo_total = time.time() - inicio
    print(f"\n¡Rainbow table completada!")
    print(f"Tiempo total: {tiempo_total:.2f} segundos ({tiempo_total/60:.2f} minutos)")
    print(f"Base de datos guardada en: {output_db}")

# Función para buscar en la rainbow table
def buscar_en_rainbow(hash_objetivo: str, db_path="rainbow_5chars.db"):
    """Busca un hash en la rainbow table y devuelve el mensaje original."""
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    inicio = time.time()
    c.execute('SELECT mensaje FROM rainbow WHERE hash = ?', (hash_objetivo,))
    resultado = c.fetchone()
    tiempo = (time.time() - inicio) * 1000  # En milisegundos

    conn.close()

    if resultado:
        print(f"¡Encontrado! Mensaje original: {resultado[0]}")
        print(f"Tiempo de búsqueda: {tiempo:.2f} ms")
        return resultado[0]
    else:
        print(f"No encontrado en la rainbow table")
        print(f"Tiempo de búsqueda: {tiempo:.2f} ms")
        return None

# Ejecutar
if __name__ == "__main__":
    # Generar la tabla (solo una vez)
    generar_rainbow_table()

    # Ejemplo de uso
    print("\n" + "="*80)
    print("Probando búsqueda en rainbow table")
    print("="*80)
    hash_ejemplo = "MTMxNzRkN2RkMGFmMGRhZDQxMjQ3MmI2Y2MwYWM0YmQ="
    buscar_en_rainbow(hash_ejemplo)
```

### Ventajas de este Proyecto

1. **Tiempo invertido**: ~3 minutos (perfecto para una clase)
2. **Almacenamiento**: ~665 MB (mínimo)
3. **Búsqueda**: Instantánea (milisegundos)
4. **Aprende**: Rainbow tables, bases de datos, indexación, trade-offs espacio-tiempo
5. **Reutilizable**: Úsala para resolver TODOS los mensajes del reto instantáneamente

## 📚 Referencias

- [Rainbow Table - Wikipedia](https://en.wikipedia.org/wiki/Rainbow_table)
- [Password Hashing Competition](https://www.password-hashing.net/)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

---

**Nota**: Este análisis es puramente educativo. En sistemas reales, NUNCA almacenes contraseñas en texto plano o uses algoritmos simples como MD5 sin salt.
