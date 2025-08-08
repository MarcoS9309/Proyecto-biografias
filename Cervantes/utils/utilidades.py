"""
Utilidades comunes para el sistema de evaluación de Cervantes.
Contiene funciones reutilizables para mostrar preguntas, calcular puntajes, etc.
"""

import random
from typing import List, Dict, Any


class ColoresCLI:
    """Códigos de colores para la terminal."""
    VERDE = '\033[92m'
    ROJO = '\033[91m'
    AZUL = '\033[94m'
    AMARILLO = '\033[93m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BLANCO = '\033[97m'
    RESET = '\033[0m'
    NEGRITA = '\033[1m'


def mostrar_pregunta(pregunta: Dict[str, Any], numero: int = None) -> None:
    """
    Muestra una pregunta formateada en la consola.
    
    Args:
        pregunta: Diccionario con la pregunta, opciones y respuesta
        numero: Número de la pregunta (opcional)
    """
    if numero:
        print(f"\n{ColoresCLI.AZUL}Pregunta {numero}:{ColoresCLI.RESET}")
    
    print(f"{ColoresCLI.NEGRITA}{pregunta['pregunta']}{ColoresCLI.RESET}")
    
    for opcion in pregunta["opciones"]:
        print(f"  {opcion}")


def obtener_respuesta_usuario() -> str:
    """
    Obtiene y valida la respuesta del usuario.
    
    Returns:
        Respuesta válida del usuario (a, b, o c)
    """
    while True:
        respuesta = input(f"\n{ColoresCLI.CYAN}Tu respuesta (a/b/c): {ColoresCLI.RESET}").strip().lower()
        if respuesta in ['a', 'b', 'c']:
            return respuesta
        print(f"{ColoresCLI.ROJO}Por favor, ingresa una opción válida (a, b, o c).{ColoresCLI.RESET}")


def mostrar_resultado(es_correcto: bool, respuesta_correcta: str = None) -> None:
    """
    Muestra el resultado de una respuesta.
    
    Args:
        es_correcto: Si la respuesta fue correcta
        respuesta_correcta: La respuesta correcta (si es incorrecta)
    """
    if es_correcto:
        mensajes_correcto = [
            "🌟 ¡Correcto!",
            "✓ ¡Excelente!",
            "👏 ¡Muy bien!",
            "🎉 ¡Perfecto!"
        ]
        print(f"{ColoresCLI.VERDE}{random.choice(mensajes_correcto)}{ColoresCLI.RESET}\n")
    else:
        print(f"{ColoresCLI.ROJO}❌ Incorrecto. La respuesta correcta es: {respuesta_correcta.upper()}{ColoresCLI.RESET}\n")


def calcular_calificacion(puntaje: int, total: int) -> str:
    """
    Calcula la calificación basada en el puntaje.
    
    Args:
        puntaje: Puntos obtenidos
        total: Total de preguntas
        
    Returns:
        Mensaje de calificación
    """
    porcentaje = (puntaje / total) * 100
    
    if porcentaje == 100:
        return f"{ColoresCLI.VERDE}🏆 ¡Excelente! Dominas la biografía cervantina{ColoresCLI.RESET}"
    elif porcentaje >= 80:
        return f"{ColoresCLI.AZUL}🌟 ¡Muy bien! Tienes un conocimiento sólido{ColoresCLI.RESET}"
    elif porcentaje >= 60:
        return f"{ColoresCLI.AMARILLO}📚 Buen trabajo, pero puedes mejorar algunos detalles{ColoresCLI.RESET}"
    else:
        return f"{ColoresCLI.MAGENTA}💪 ¡Ánimo! Revisa la biografía con más atención{ColoresCLI.RESET}"


def mostrar_retroalimentacion(preguntas: List[Dict], respuestas_usuario: List[str]) -> None:
    """
    Muestra retroalimentación específica para respuestas incorrectas.
    
    Args:
        preguntas: Lista de preguntas
        respuestas_usuario: Lista de respuestas del usuario
    """
    print(f"\n{ColoresCLI.CYAN}RETROALIMENTACIÓN:{ColoresCLI.RESET}")
    
    hay_errores = False
    for i, (pregunta, respuesta_usuario) in enumerate(zip(preguntas, respuestas_usuario)):
        if respuesta_usuario != pregunta["respuesta"]:
            hay_errores = True
            retroalimentacion = pregunta.get("retroalimentacion", "Revisa este tema con más detalle")
            print(f"- {ColoresCLI.AMARILLO}Pregunta {i+1}:{ColoresCLI.RESET} {retroalimentacion}")
    
    if not hay_errores:
        print(f"{ColoresCLI.VERDE}¡Perfecto! No hay errores que revisar.{ColoresCLI.RESET}")


def mostrar_encabezado(titulo: str) -> None:
    """
    Muestra un encabezado decorativo.
    
    Args:
        titulo: Título a mostrar
    """
    separador = "=" * 50
    print(f"\n{ColoresCLI.NEGRITA}{separador}")
    print(f"{titulo.center(50)}")
    print(f"{separador}{ColoresCLI.RESET}\n")


def mostrar_dato_curioso(datos_curiosos: List[str]) -> None:
    """
    Muestra un dato curioso aleatorio.
    
    Args:
        datos_curiosos: Lista de datos curiosos
    """
    dato = random.choice(datos_curiosos)
    print(f"\n{ColoresCLI.CYAN}💡 Dato curioso:{ColoresCLI.RESET}")
    print(f"{ColoresCLI.BLANCO}{dato}{ColoresCLI.RESET}")


def pausar() -> None:
    """Pausa la ejecución hasta que el usuario presione Enter."""
    input(f"\n{ColoresCLI.MAGENTA}Presiona Enter para continuar...{ColoresCLI.RESET}")
