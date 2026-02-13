"""
Solución al reto de fuerza bruta para encontrar mensajes originales de 4 caracteres.

Este script demuestra cómo usar fuerza bruta para descifrar mensajes que fueron
procesados a través del pipeline: Caesar → ROT13 → SHA256 → MD5 → Base64

Uso:
    # Usar el hash por defecto definido en el código
    uv run python solucion.py

    # Proporcionar un hash personalizado como argumento
    uv run python solucion.py "MTAyMGY5OGQ5OTdhYTdjZDRmODI1NGU2N2ZlODM2MmI="

El script mostrará:
    - Progreso cada 10,000 intentos
    - Tiempo transcurrido durante la búsqueda
    - Velocidad de procesamiento (intentos/segundo)
    - Tiempo total de ejecución
"""

import string
import itertools
import sys
import time
from utils import caesar_cipher, rot13_cipher, sha256_hash, md5_hash, base64_encode


# Mensaje cifrado objetivo (en Base64) - Ejemplo del README
# Pista: "Comienza con una letra del inicio del alfabeto"
MENSAJE_CIFRADO_OBJETIVO = "MDY5ZGFmNDQ0ZmZjOTZjNmQzN2E3YmY1Nzc4NDY4MTg="


def aplicar_pipeline_completo(mensaje: str) -> str:
    """
    Aplica el pipeline completo de transformaciones al mensaje.

    Pipeline: Caesar(shift=3) → ROT13 → SHA256 → MD5 → Base64

    Args:
        mensaje: Mensaje original de 4 caracteres

    Returns:
        Resultado final en Base64
    """
    # 1. Caesar cipher con desplazamiento de 3
    paso1 = caesar_cipher(mensaje, shift=3)

    # 2. ROT13
    paso2 = rot13_cipher(paso1)

    # 3. SHA256 hash
    paso3 = sha256_hash(paso2)

    # 4. MD5 hash
    paso4 = md5_hash(paso3)

    # 5. Base64 encoding
    resultado_final = base64_encode(paso4)

    return resultado_final


def generar_candidatos(longitud: int = 4):
    """
    Genera todos los candidatos posibles de longitud especificada.

    Usa letras minúsculas (a-z) y números (0-9).
    Total de combinaciones para 4 caracteres: 36^4 = 1,679,616

    Args:
        longitud: Longitud del mensaje candidato

    Yields:
        Cada candidato posible como string
    """
    # Caracteres permitidos: letras minúsculas y números
    caracteres = string.ascii_lowercase + string.digits  # 'abcdefghijklmnopqrstuvwxyz0123456789'

    # Generar todas las combinaciones posibles
    for combinacion in itertools.product(caracteres, repeat=longitud):
        yield ''.join(combinacion)


def buscar_mensaje_original(objetivo: str, mostrar_progreso: bool = True) -> tuple[str | None, float]:
    """
    Busca el mensaje original de 4 caracteres usando fuerza bruta.

    Args:
        objetivo: Mensaje cifrado en Base64 que queremos descifrar
        mostrar_progreso: Si se debe mostrar el progreso cada 10,000 intentos

    Returns:
        Tupla con (mensaje original si se encuentra o None, tiempo transcurrido en segundos)
    """
    print("=" * 80)
    print("BÚSQUEDA POR FUERZA BRUTA")
    print("=" * 80)
    print(f"\nObjetivo: {objetivo}")
    print(f"Total de combinaciones a probar: 36^4 = 1,679,616")
    print("\nIniciando búsqueda...\n")

    # Registrar tiempo de inicio
    tiempo_inicio = time.time()
    intentos = 0

    for candidato in generar_candidatos(longitud=4):
        intentos += 1

        # Mostrar progreso cada 10,000 intentos
        if mostrar_progreso and intentos % 10000 == 0:
            tiempo_transcurrido = time.time() - tiempo_inicio
            print(f"Progreso: {intentos:,} intentos... (último probado: {candidato}) - Tiempo: {tiempo_transcurrido:.2f}s")

        # Aplicar el pipeline completo al candidato
        resultado = aplicar_pipeline_completo(candidato)

        # Verificar si coincide con el objetivo
        if resultado == objetivo:
            tiempo_total = time.time() - tiempo_inicio
            print("\n" + "=" * 80)
            print("¡MENSAJE ENCONTRADO!")
            print("=" * 80)
            print(f"\nMensaje original: {candidato}")
            print(f"Intentos realizados: {intentos:,}")
            print(f"Tiempo transcurrido: {tiempo_total:.2f} segundos ({tiempo_total:.4f}s)")
            print(f"Velocidad: {intentos/tiempo_total:,.0f} intentos/segundo")
            print(f"\nVerificación del pipeline:")
            print(f"  1. Original:        {candidato}")
            print(f"  2. Caesar(shift=3): {caesar_cipher(candidato, shift=3)}")
            print(f"  3. ROT13:           {rot13_cipher(caesar_cipher(candidato, shift=3))}")
            paso3 = rot13_cipher(caesar_cipher(candidato, shift=3))
            print(f"  4. SHA256:          {sha256_hash(paso3)}")
            print(f"  5. MD5:             {md5_hash(sha256_hash(paso3))}")
            print(f"  6. Base64:          {resultado}")
            print("=" * 80)
            return candidato, tiempo_total

    # Si no se encuentra después de probar todas las combinaciones
    tiempo_total = time.time() - tiempo_inicio
    print("\n" + "=" * 80)
    print("Mensaje no encontrado después de probar todas las combinaciones.")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")
    print("=" * 80)
    return None, tiempo_total


def buscar_mensaje_con_prefijo(objetivo: str, prefijo: str) -> tuple[str | None, float]:
    """
    Busca el mensaje original que comienza con un prefijo específico.

    Útil para dividir el trabajo en equipos - cada persona busca con un prefijo diferente.

    Args:
        objetivo: Mensaje cifrado en Base64
        prefijo: Los primeros caracteres del mensaje (ej: "a", "ab", "abc")

    Returns:
        Tupla con (mensaje original si se encuentra o None, tiempo transcurrido en segundos)
    """
    print(f"\nBuscando mensajes que comienzan con '{prefijo}'...")
    tiempo_inicio = time.time()

    # Calcular cuántos caracteres faltan
    caracteres_restantes = 4 - len(prefijo)
    caracteres = string.ascii_lowercase + string.digits

    intentos = 0

    for combinacion in itertools.product(caracteres, repeat=caracteres_restantes):
        candidato = prefijo + ''.join(combinacion)
        intentos += 1

        if intentos % 5000 == 0:
            tiempo_transcurrido = time.time() - tiempo_inicio
            print(f"  Probando: {candidato} ({intentos:,} intentos) - Tiempo: {tiempo_transcurrido:.2f}s")

        resultado = aplicar_pipeline_completo(candidato)

        if resultado == objetivo:
            tiempo_total = time.time() - tiempo_inicio
            print(f"\n¡Encontrado! Mensaje: {candidato} (intentos: {intentos:,}, tiempo: {tiempo_total:.2f}s)")
            return candidato, tiempo_total

    tiempo_total = time.time() - tiempo_inicio
    print(f"  No encontrado con prefijo '{prefijo}' ({intentos:,} combinaciones probadas, tiempo: {tiempo_total:.2f}s)")
    return None, tiempo_total


def main():
    """Función principal para ejecutar la búsqueda."""

    # Verificar si se proporcionó un hash como argumento
    if len(sys.argv) > 1:
        # Usar el hash proporcionado por línea de comandos
        objetivo = sys.argv[1]
        print(f"\n📥 Hash recibido por argumento: {objetivo}")
    else:
        # Usar el hash por defecto
        objetivo = MENSAJE_CIFRADO_OBJETIVO
        print("\n📌 Usando hash por defecto del código")

    # Registrar tiempo total de ejecución del script
    tiempo_inicio_script = time.time()

    # Búsqueda completa (puede tardar 15-30 segundos)
    print("\n🔍 Iniciando búsqueda por fuerza bruta...")
    mensaje_encontrado, tiempo_busqueda = buscar_mensaje_original(
        objetivo,
        mostrar_progreso=True
    )

    tiempo_total_script = time.time() - tiempo_inicio_script

    if mensaje_encontrado:
        print(f"\n✅ ¡Éxito! El mensaje original es: {mensaje_encontrado}")
        print(f"\n⏱️  Tiempo de búsqueda: {tiempo_busqueda:.2f} segundos")
    else:
        print("\n❌ No se pudo encontrar el mensaje.")
        print(f"\n⏱️  Tiempo de búsqueda: {tiempo_busqueda:.2f} segundos")

    print(f"⏱️  Tiempo total de ejecución: {tiempo_total_script:.2f} segundos")

    # Opción 2: Búsqueda dividida por prefijo (descomenta para usar)
    # print("\n🔍 Búsqueda dividida - probando con prefijos específicos...")
    # for letra in ['a', 'b', 'c']:  # Cada persona del equipo busca con una letra
    #     resultado, tiempo = buscar_mensaje_con_prefijo(objetivo, letra)
    #     if resultado:
    #         print(f"✅ Encontrado con prefijo '{letra}': {resultado} en {tiempo:.2f}s")
    #         break


if __name__ == "__main__":
    main()
