"""
Menú principal del sistema de evaluación y chatbot sobre Cervantes.
Punto de entrada único para todas las funcionalidades del proyecto.
"""

import sys
import os

# Agregar el directorio actual al path para importar módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.utilidades import ColoresCLI, mostrar_encabezado
from evaluadores.evaluador_basico import EvaluadorCervantes
from evaluadores.evaluador_avanzado import EvaluadorAvanzado
from chatbot.chatbot_principal import ChatbotCervantes


class MenuPrincipal:
    """Clase principal para el menú del sistema."""
    
    def __init__(self):
        self.opciones = {
            '1': self._ejecutar_evaluacion_basica,
            '2': self._ejecutar_evaluacion_avanzada,
            '3': self._ejecutar_chatbot,
            '4': self._mostrar_informacion,
            '5': self._salir
        }
    
    def mostrar_menu(self) -> None:
        """Muestra el menú principal y maneja la navegación."""
        while True:
            self._imprimir_menu()
            opcion = input(f"{ColoresCLI.CYAN}Selecciona una opción (1-5): {ColoresCLI.RESET}").strip()
            
            if opcion in self.opciones:
                if opcion == '5':
                    self.opciones[opcion]()
                    break
                else:
                    self._ejecutar_opcion(opcion)
            else:
                print(f"{ColoresCLI.ROJO}Opción no válida. Por favor, selecciona del 1 al 5.{ColoresCLI.RESET}")
    
    def _imprimir_menu(self) -> None:
        """Imprime el menú de opciones."""
        mostrar_encabezado("SISTEMA CERVANTINO INTERACTIVO")
        
        print(f"{ColoresCLI.AZUL}┌─ Opciones disponibles ─────────────────────────┐{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AZUL}│{ColoresCLI.RESET} {ColoresCLI.VERDE}1.{ColoresCLI.RESET} Evaluación Básica sobre Cervantes          {ColoresCLI.AZUL}│{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AZUL}│{ColoresCLI.RESET} {ColoresCLI.AMARILLO}2.{ColoresCLI.RESET} Modo Desafío (Evaluación Avanzada)        {ColoresCLI.AZUL}│{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AZUL}│{ColoresCLI.RESET} {ColoresCLI.MAGENTA}3.{ColoresCLI.RESET} Chatbot Interactivo                        {ColoresCLI.AZUL}│{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AZUL}│{ColoresCLI.RESET} {ColoresCLI.CYAN}4.{ColoresCLI.RESET} Información del Proyecto                   {ColoresCLI.AZUL}│{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AZUL}│{ColoresCLI.RESET} {ColoresCLI.ROJO}5.{ColoresCLI.RESET} Salir                                      {ColoresCLI.AZUL}│{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AZUL}└────────────────────────────────────────────────┘{ColoresCLI.RESET}")
    
    def _ejecutar_opcion(self, opcion: str) -> None:
        """
        Ejecuta la opción seleccionada y maneja errores.
        
        Args:
            opcion: Opción seleccionada por el usuario
        """
        try:
            self.opciones[opcion]()
            self._pausar_antes_de_continuar()
        except KeyboardInterrupt:
            print(f"\n{ColoresCLI.AMARILLO}Operación interrumpida por el usuario.{ColoresCLI.RESET}")
            self._pausar_antes_de_continuar()
        except Exception as e:
            print(f"\n{ColoresCLI.ROJO}Error inesperado: {e}{ColoresCLI.RESET}")
            self._pausar_antes_de_continuar()
    
    def _ejecutar_evaluacion_basica(self) -> None:
        """Ejecuta la evaluación básica."""
        evaluador = EvaluadorCervantes()
        evaluador.ejecutar_evaluacion()
    
    def _ejecutar_evaluacion_avanzada(self) -> None:
        """Ejecuta la evaluación avanzada (modo desafío)."""
        evaluador = EvaluadorAvanzado()
        evaluador.ejecutar_desafio()
    
    def _ejecutar_chatbot(self) -> None:
        """Ejecuta el chatbot interactivo."""
        chatbot = ChatbotCervantes()
        chatbot.iniciar_conversacion()
    
    def _mostrar_informacion(self) -> None:
        """Muestra información sobre el proyecto."""
        mostrar_encabezado("INFORMACIÓN DEL PROYECTO")
        
        info = f"""
{ColoresCLI.CYAN}📚 Sistema Cervantino Interactivo{ColoresCLI.RESET}

{ColoresCLI.VERDE}Descripción:{ColoresCLI.RESET}
Este proyecto es un sistema educativo interactivo dedicado a Miguel de Cervantes,
el gran escritor español autor de Don Quijote de la Mancha.

{ColoresCLI.VERDE}Funcionalidades:{ColoresCLI.RESET}
• {ColoresCLI.AZUL}Evaluación Básica:{ColoresCLI.RESET} Test de conocimientos fundamentales sobre la vida y obra de Cervantes
• {ColoresCLI.AMARILLO}Modo Desafío:{ColoresCLI.RESET} Preguntas avanzadas con orden aleatorio para expertos
• {ColoresCLI.MAGENTA}Chatbot Interactivo:{ColoresCLI.RESET} Conversación empática sobre literatura y temas generales

{ColoresCLI.VERDE}Características:{ColoresCLI.RESET}
• Interfaz colorida y amigable
• Retroalimentación educativa personalizada
• Datos curiosos sobre Cervantes
• Conversación natural con el chatbot

{ColoresCLI.VERDE}Objetivo:{ColoresCLI.RESET}
Fomentar el aprendizaje sobre uno de los escritores más importantes de la literatura
universal de manera interactiva y divertida.

{ColoresCLI.CYAN}💡 ¡Disfruta explorando el mundo cervantino!{ColoresCLI.RESET}
        """
        
        print(info)
    
    def _salir(self) -> None:
        """Muestra mensaje de despedida."""
        print(f"\n{ColoresCLI.VERDE}¡Gracias por usar el Sistema Cervantino Interactivo!{ColoresCLI.RESET}")
        print(f"{ColoresCLI.CYAN}Que la sabiduría de Cervantes te acompañe siempre.{ColoresCLI.RESET}")
        print(f"{ColoresCLI.AMARILLO}¡Hasta pronto! 📚✨{ColoresCLI.RESET}")
    
    def _pausar_antes_de_continuar(self) -> None:
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input(f"\n{ColoresCLI.MAGENTA}Presiona Enter para volver al menú principal...{ColoresCLI.RESET}")


def main():
    """Función principal del programa."""
    try:
        menu = MenuPrincipal()
        menu.mostrar_menu()
    except KeyboardInterrupt:
        print(f"\n\n{ColoresCLI.AMARILLO}¡Hasta pronto!{ColoresCLI.RESET}")
    except Exception as e:
        print(f"\n{ColoresCLI.ROJO}Error crítico: {e}{ColoresCLI.RESET}")


if __name__ == "__main__":
    main()
