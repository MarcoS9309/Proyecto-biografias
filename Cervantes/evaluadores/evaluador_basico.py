"""
Evaluador básico de conocimientos sobre Cervantes.
Versión refactorizada y mejorada del sistema de evaluación.
"""

import sys
import os

# Agregar el directorio padre al path para importar módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from data.preguntas_cervantes import PREGUNTAS_BASICAS, DATOS_CURIOSOS
from utils.utilidades import (
    mostrar_encabezado, mostrar_pregunta, obtener_respuesta_usuario,
    mostrar_resultado, calcular_calificacion, mostrar_retroalimentacion,
    mostrar_dato_curioso, ColoresCLI
)


class EvaluadorCervantes:
    """Clase principal para el evaluador de conocimientos sobre Cervantes."""
    
    def __init__(self):
        self.preguntas = PREGUNTAS_BASICAS.copy()
        self.puntaje = 0
        self.respuestas_usuario = []
    
    def ejecutar_evaluacion(self) -> None:
        """Ejecuta la evaluación completa."""
        mostrar_encabezado("EVALUACIÓN DE CONOCIMIENTOS SOBRE CERVANTES")
        
        # Realizar preguntas
        for i, pregunta in enumerate(self.preguntas, 1):
            mostrar_pregunta(pregunta, i)
            respuesta = obtener_respuesta_usuario()
            self.respuestas_usuario.append(respuesta)
            
            es_correcto = respuesta == pregunta["respuesta"]
            if es_correcto:
                self.puntaje += 1
            
            mostrar_resultado(es_correcto, pregunta["respuesta"])
        
        # Mostrar resultados finales
        self._mostrar_resultados_finales()
    
    def _mostrar_resultados_finales(self) -> None:
        """Muestra los resultados finales y retroalimentación."""
        print("\n" + "=" * 50)
        print(f"{ColoresCLI.NEGRITA}PUNTAJE FINAL: {self.puntaje}/{len(self.preguntas)}{ColoresCLI.RESET}")
        
        # Mostrar calificación
        calificacion = calcular_calificacion(self.puntaje, len(self.preguntas))
        print(f"\n{calificacion}")
        
        # Mostrar retroalimentación
        mostrar_retroalimentacion(self.preguntas, self.respuestas_usuario)
        
        # Mostrar dato curioso
        mostrar_dato_curioso(DATOS_CURIOSOS)


def main():
    """Función principal."""
    try:
        evaluador = EvaluadorCervantes()
        evaluador.ejecutar_evaluacion()
    except KeyboardInterrupt:
        print(f"\n\n{ColoresCLI.AMARILLO}Evaluación interrumpida. ¡Hasta pronto!{ColoresCLI.RESET}")
    except Exception as e:
        print(f"\n{ColoresCLI.ROJO}Error inesperado: {e}{ColoresCLI.RESET}")


if __name__ == "__main__":
    main()
