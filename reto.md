# 🎯 Reto Avanzado: Descifrar Mensajes de 6 Caracteres

Este es un reto avanzado de fuerza bruta para descifrar mensajes de **6 caracteres** que fueron procesados a través del pipeline completo de transformaciones.

## 📋 Características del Reto

### Parámetros del Mensaje Original
- **Longitud**: Exactamente 6 caracteres
- **Caracteres permitidos**:
  - Letras mayúsculas (A-Z): 26 caracteres
  - Letras minúsculas (a-z): 26 caracteres
  - Números (0-9): 10 caracteres
  - **Total**: 62 caracteres posibles por posición

### Espacio de Búsqueda
```
Total de combinaciones = 62^6 = 56,800,235,584 (56.8 mil millones)
```

⚠️ **Advertencia**: Este reto es significativamente más difícil que el original. Con 56.8 mil millones de combinaciones, la fuerza bruta completa puede tardar:
- **Sin optimización**: Varios días o semanas
- **Con paralelización (8 núcleos)**: Varios días
- **Usando las pistas**: Mucho más rápido

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
| 1 | `NDI4MTZmOTU2NTRiODk3MTQ2NGRkZjVmMDMyMDQ0YTE=` | Lenguaje de programación | 6 caracteres |
| 2 | `ZWQ3OTAwN2UzZjQ3NTdjYTRhNDk1MGU0M2Q3Y2UyZTI=` | Plataforma de código | 6 caracteres |
| 3 | `NDBkMmE0MTBkNzQ2NmRlYTE5NmUzYzc4N2UwZDc3ZDk=` | Contenedores | 6 caracteres |
| 4 | `NmQ4YjMzNDgwMDM3YTRkMTFjMGJlNzU4ZTE4OGQ0OTk=` | Infraestructura | 6 caracteres |
| 5 | `OWM0ZWE3YjM4N2QyYWI4NWRhM2IwY2FjYmYyMDRlMTE=` | Frontend | 6 caracteres |
| 6 | `OWY4YmFhNTBjMmM4NDRlYjA4YTU1ZWUwYmI3MGVmMmI=` | Análisis de datos | 6 caracteres |
| 7 | `NDc4NWNhNjQ1N2VmODM1OWYyZDg4ZjZhYTczZmU1NzM=` | Puesta en producción | 6 caracteres |
| 8 | `N2ZlYmJkNGQ5YTFlZGFhYWFmZWQwZTAyMDk2YjhmNDc=` | Función sin servidor | 6 caracteres |
| 9 | `NDMyN2I5N2IwNjljOTM5MjE0ZTA1YWIwYjAxNDI2ZTY=` | Redes de IA | 6 caracteres |
| 10 | `NGU0Y2ZmOTdlNjYyZjE0NzljMWVhNDA1MzlkYmU1Y2E=` | Servidor web | 6 caracteres |
| 11 | `NTY5ZDY3OTBkY2RkZWQ4MGU5MDk0MGNmNTc3MTkxNGM=` | Sistema operativo | 6 caracteres |
| 12 | `MmQ0MDNiMDU5NDE3NDA5MGM1NGE0MTQ3ZWMwZjgyNzE=` | Núcleo del OS | 6 caracteres |
| 13 | `ZTc1MjFmMjVmOWE2ZGU5YTMxYTFkYjlkZjEyNDZjMTM=` | Código máquina | 6 caracteres |
| 14 | `NzY1YTBjNTc5NjM2YzllZGM2MjRlOTQwYTE1YTY4NDU=` | Red de dispositivos | 6 caracteres |
| 15 | `OGU4ZDkwNDFkZGM0ZmNiOTM5MWU3MTA4NDgxYmYwNDQ=` | Comunicación de red | 6 caracteres |
| 16 | `Y2I0OWE4ZDEyYmE4YjkxYTQzYzI4YzU4YTk4NDk4ZTM=` | Rama principal | 6 caracteres |
| 17 | `YTJmZmJjZTY5ZjA2YzJiYWNkYzY2MzAzMDI4Nzk1NTg=` | Repositorio remoto | 6 caracteres |
| 18 | `MTAxMjA2MGFkMjQzMTY1NGEzNDM4YTRhNDk4NGY4ZDQ=` | Guardar cambios | 6 caracteres |
| 19 | `ZjIwMzY4Mzk5NTMwOTVjMDI1Y2VjODY3NTAwYzRhNzQ=` | Rama de código | 6 caracteres |
| 20 | `NWZlZTcyYjU0MmY0YTNkNTJlNTcwM2M3MzFjNDg0ZTY=` | Criptografía | 6 caracteres |

## 💡 Estrategias Recomendadas

### 1. Usar las Pistas
Las pistas te dan información sobre el mensaje original. Por ejemplo:
- "Lenguaje de programación" → probablemente sea "Python", "Java", etc.
- "Plataforma de código" → probablemente sea "GitHub", "GitLab", etc.

### 2. Búsqueda Basada en Diccionario
En lugar de fuerza bruta completa, crea una lista de palabras candidatas relacionadas con la pista:

```python
# Ejemplo para el mensaje #1 (Lenguaje de programación)
candidatos = ["Python", "JavaSc", "Kotlin", "GoLang", "Elixir", "Erlang", ...]

for candidato in candidatos:
    resultado = aplicar_pipeline_completo(candidato)
    if resultado == objetivo:
        print(f"¡Encontrado! {candidato}")
```

### 3. Trabajo en Equipo
Dividan los mensajes entre el equipo:
- Persona 1: Mensajes 1-5
- Persona 2: Mensajes 6-10
- Persona 3: Mensajes 11-15
- Persona 4: Mensajes 16-20

### 4. Caso Sensible
Recuerda que estos mensajes distinguen entre mayúsculas y minúsculas:
- "python" ≠ "Python" ≠ "PYTHON"

Basándote en las pistas, puedes inferir el caso correcto:
- Nombres propios → Primera letra mayúscula (Python, Docker, GitHub)
- Siglas → Todo mayúsculas (API, SQL, DNS)
- Términos técnicos → Todo minúsculas (server, client, socket)

## 🚀 Cómo Ejecutar

### Modificar solucion.py para 6 caracteres

Necesitarás modificar el archivo `solucion.py` para manejar 6 caracteres y los nuevos tipos de caracteres:

```python
# Cambiar en generar_candidatos():
caracteres = string.ascii_letters + string.digits  # Mayúsculas, minúsculas y números

# Cambiar la longitud:
for combinacion in itertools.product(caracteres, repeat=6):  # 6 en lugar de 4
```

### Ejecutar con un Hash Específico

```bash
# Ejemplo: Descifrar el primer mensaje
uv run python solucion.py "NDI4MTZmOTU2NTRiODk3MTQ2NGRkZjVmMDMyMDQ0YTE="
```

## ⏱️ Estimación de Tiempo

- **Fuerza bruta completa**: No práctico (semanas/meses)
- **Búsqueda con diccionario inteligente**: Segundos a minutos
- **Búsqueda combinada** (pistas + patrones comunes): Minutos

## 🏆 Desafío Extra

Una vez que descifres los 20 mensajes, intenta:
1. Documentar tu estrategia de resolución
2. Medir cuánto tiempo tardaste en cada mensaje
3. Crear tu propio generador de retos
4. Implementar paralelización para acelerar la búsqueda

---

**Suerte con el reto** 🚀 Recuerda: la clave está en usar las pistas de manera inteligente en lugar de fuerza bruta pura.
