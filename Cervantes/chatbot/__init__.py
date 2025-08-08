"""
Módulo del chatbot para el sistema Cervantino.
Contiene el chatbot interactivo y sus respuestas.
"""

from .chatbot_principal import ChatbotCervantes
from .respuestas_bot import (
    obtener_saludo, obtener_despedida, obtener_comentario_correcto,
    obtener_comentario_incorrecto, obtener_respuesta_generica
)

__all__ = [
    'ChatbotCervantes', 'obtener_saludo', 'obtener_despedida',
    'obtener_comentario_correcto', 'obtener_comentario_incorrecto',
    'obtener_respuesta_generica'
]
