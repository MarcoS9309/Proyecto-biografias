"""Prueba funcional básica del EvaluadorCervantes.
Verifica que el flujo de evaluación básica funciona con entradas simuladas.
"""

import builtins
from evaluadores.evaluador_basico import EvaluadorCervantes


def test_flujo_evaluacion_basica(monkeypatch):
    # Simular respuestas: todas 'a' para recorrer flujo completo
    respuestas = iter(['a','a','a','a','a','a'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(respuestas))

    evaluador = EvaluadorCervantes()
    evaluador.ejecutar_evaluacion()

    # Asegurar que se registraron 6 respuestas
    assert len(evaluador.respuestas_usuario) == 6
    # Puntaje debe ser entre 0 y 6
    assert 0 <= evaluador.puntaje <= 6
