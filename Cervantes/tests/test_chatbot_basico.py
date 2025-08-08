"""Prueba funcional mínima del ChatbotCervantes.
Simula interacción básica con el chatbot (una pregunta y salida).
"""

import builtins
from chatbot.chatbot_principal import ChatbotCervantes


def test_flujo_chatbot(monkeypatch):
    # Secuencia: pedir pregunta, responder 'a', luego decir adios
    entradas = iter(['pregunta', 'a', 'adios'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(entradas))

    bot = ChatbotCervantes()
    bot.iniciar_conversacion()

    # Conversación debe haber terminado
    assert bot.conversacion_activa is False
