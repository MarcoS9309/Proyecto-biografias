"""
Módulo de utilidades para el sistema Cervantino.
Contiene funciones comunes y herramientas de apoyo.
"""

from .utilidades import (
    ColoresCLI, mostrar_pregunta, obtener_respuesta_usuario,
    mostrar_resultado, calcular_calificacion, mostrar_retroalimentacion,
    mostrar_encabezado, mostrar_dato_curioso, pausar
)

__all__ = [
    'ColoresCLI', 'mostrar_pregunta', 'obtener_respuesta_usuario',
    'mostrar_resultado', 'calcular_calificacion', 'mostrar_retroalimentacion',
    'mostrar_encabezado', 'mostrar_dato_curioso', 'pausar'
]
