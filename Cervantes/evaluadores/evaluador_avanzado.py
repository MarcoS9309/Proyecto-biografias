"""
Evaluador avanzado (Modo Desafío) de conocimientos sobre Cervantes.
Versión refactorizada con preguntas más complejas y orden aleatorio.
"""

import random
import sys
import os

# Agregar el directorio padre al path para importar módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from data.preguntas_cervantes import PREGUNTAS_AVANZADAS, DATOS_CURIOSOS
from utils.utilidades import (
    mostrar_encabezado, mostrar_pregunta, obtener_respuesta_usuario,
    mostrar_resultado, mostrar_dato_curioso, ColoresCLI
)


class EvaluadorAvanzado:
    """Clase para el evaluador avanzado (modo desafío) sobre Cervantes."""
    
    def __init__(self):
        self.preguntas = PREGUNTAS_AVANZADAS.copy()
        random.shuffle(self.preguntas)  # Orden aleatorio para mayor desafío
        self.puntaje = 0
        self.respuestas_usuario = []
    
    def ejecutar_desafio(self) -> None:
        """Ejecuta el modo desafío completo."""
        mostrar_encabezado("MODO DESAFÍO: CERVANTES")
        print(f"{ColoresCLI.AMARILLO}¡Pon a prueba tu conocimiento avanzado!{ColoresCLI.RESET}\n")
        
        # Realizar preguntas
        for i, pregunta in enumerate(self.preguntas, 1):
            print(f"{ColoresCLI.MAGENTA}Desafío {i}:{ColoresCLI.RESET}")
            mostrar_pregunta(pregunta)
            respuesta = obtener_respuesta_usuario()
            self.respuestas_usuario.append(respuesta)
            
            es_correcto = respuesta == pregunta["respuesta"]
            if es_correcto:
                self.puntaje += 1
            
            mostrar_resultado(es_correcto, pregunta["respuesta"])
        
        # Mostrar resultados finales
        self._mostrar_resultados_desafio()
    
    def _mostrar_resultados_desafio(self) -> None:
        """Muestra los resultados del modo desafío."""
        print("\n" + "=" * 50)
        print(f"{ColoresCLI.NEGRITA}PUNTAJE FINAL DESAFÍO: {self.puntaje}/{len(self.preguntas)}{ColoresCLI.RESET}")
        
        # Calificaciones específicas del modo desafío
        porcentaje = (self.puntaje / len(self.preguntas)) * 100
        
        if porcentaje == 100:
            mensaje = f"{ColoresCLI.VERDE}🏆 ¡Eres un cervantista experto!{ColoresCLI.RESET}"
        elif porcentaje >= 80:
            mensaje = f"{ColoresCLI.AZUL}🔍 ¡Excelente! Dominas los detalles avanzados{ColoresCLI.RESET}"
        elif porcentaje >= 60:
            mensaje = f"{ColoresCLI.AMARILLO}🔎 Buen trabajo, pero Cervantes aún guarda secretos para ti{ColoresCLI.RESET}"
        else:
            mensaje = f"{ColoresCLI.MAGENTA}📚 ¡Ánimo! La lectura te hará maestro{ColoresCLI.RESET}"
        
        print(f"\n{mensaje}")
        
        # Mostrar dato curioso
        mostrar_dato_curioso(DATOS_CURIOSOS)
        
        # Retroalimentación específica para el modo desafío
        self._mostrar_retroalimentacion_avanzada()
    
    def _mostrar_retroalimentacion_avanzada(self) -> None:
        """Muestra retroalimentación específica para el modo avanzado."""
        errores = sum(1 for i, pregunta in enumerate(self.preguntas) 
                     if self.respuestas_usuario[i] != pregunta["respuesta"])
        
        if errores == 0:
            print(f"\n{ColoresCLI.VERDE}¡Perfecto! Has demostrado un conocimiento excepcional sobre Cervantes.{ColoresCLI.RESET}")
        elif errores <= 2:
            print(f"\n{ColoresCLI.AZUL}Casi perfecto. Solo algunos detalles por pulir.{ColoresCLI.RESET}")
        else:
            print(f"\n{ColoresCLI.AMARILLO}Te recomiendo profundizar en la biografía y obras de Cervantes.{ColoresCLI.RESET}")


def main():
    """Función principal."""
    try:
        evaluador = EvaluadorAvanzado()
        evaluador.ejecutar_desafio()
    except KeyboardInterrupt:
        print(f"\n\n{ColoresCLI.AMARILLO}Desafío interrumpido. ¡Hasta pronto!{ColoresCLI.RESET}")
    except Exception as e:
        print(f"\n{ColoresCLI.ROJO}Error inesperado: {e}{ColoresCLI.RESET}")


if __name__ == "__main__":
    main()
