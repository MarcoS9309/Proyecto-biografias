"""
Chatbot interactivo sobre Cervantes con capacidad de conversación humana y empática.
Versión refactorizada y mejorada con mejor organización y funcionalidades.
"""

import random
import sys
import os

# Agregar el directorio padre al path para importar módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from data.preguntas_cervantes import PREGUNTAS_AVANZADAS, DATOS_CURIOSOS
from chatbot.respuestas_bot import (
    RESPUESTAS_EMOCIONES, RESPUESTAS_INTERESES, RESPUESTAS_CONTEXTO,
    obtener_saludo, obtener_despedida, obtener_comentario_correcto,
    obtener_comentario_incorrecto, obtener_respuesta_generica
)
from utils.utilidades import ColoresCLI, mostrar_encabezado


class ChatbotCervantes:
    """Chatbot interactivo para conversar sobre Cervantes y temas generales."""
    
    def __init__(self):
        self.preguntas = PREGUNTAS_AVANZADAS.copy()
        self.datos_curiosos = DATOS_CURIOSOS.copy()
        self.nombre_usuario = None
        self.conversacion_activa = True
    
    def iniciar_conversacion(self) -> None:
        """Inicia la conversación con el usuario."""
        mostrar_encabezado("CHATBOT CERVANTINO INTERACTIVO")
        print(f"Bot: {obtener_saludo()}")
        
        while self.conversacion_activa:
            try:
                mensaje = input(f"\n{ColoresCLI.CYAN}Tú: {ColoresCLI.RESET}").strip()
                if mensaje:
                    self._procesar_mensaje(mensaje.lower())
            except KeyboardInterrupt:
                print(f"\n\n{ColoresCLI.AMARILLO}¡Hasta pronto!{ColoresCLI.RESET}")
                break
            except Exception as e:
                print(f"\n{ColoresCLI.ROJO}Error: {e}{ColoresCLI.RESET}")
    
    def _procesar_mensaje(self, mensaje: str) -> None:
        """
        Procesa el mensaje del usuario y genera una respuesta apropiada.
        
        Args:
            mensaje: Mensaje del usuario en minúsculas
        """
        # Despedidas
        if any(despedida in mensaje for despedida in ["adios", "hasta luego", "bye", "salir", "chao"]):
            print(f"Bot: {obtener_despedida()}")
            self.conversacion_activa = False
            return
        
        # Saludos
        if any(saludo in mensaje for saludo in ["hola", "buenas", "hey", "hi"]):
            print(f"Bot: {obtener_saludo()}")
            return
        
        # Preguntas sobre Cervantes
        if any(palabra in mensaje for palabra in ["pregunta", "siguiente", "otra", "quiz"]):
            self._hacer_pregunta()
            return
        
        # Datos curiosos
        if any(palabra in mensaje for palabra in ["curioso", "dato", "anécdota", "historia"]):
            self._contar_dato_curioso()
            return
        
        # Responder a emociones
        if self._responder_emocion(mensaje):
            return
        
        # Responder a intereses
        if self._responder_interes(mensaje):
            return
        
        # Responder sobre contexto cervantino
        if self._responder_contexto(mensaje):
            return
        
        # Respuesta genérica
        print(f"Bot: {obtener_respuesta_generica()}")
    
    def _hacer_pregunta(self) -> None:
        """Hace una pregunta sobre Cervantes al usuario."""
        pregunta = random.choice(self.preguntas)
        
        print(f"\nBot: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(f"  {opcion}")
        
        respuesta = input(f"{ColoresCLI.CYAN}Tu respuesta (a/b/c): {ColoresCLI.RESET}").strip().lower()
        
        if respuesta == pregunta["respuesta"]:
            print(f"Bot: {obtener_comentario_correcto()}")
        else:
            print(f"Bot: {obtener_comentario_incorrecto(pregunta['respuesta'])}")
        
        print("Bot: ¿Quieres otra pregunta? Escribe 'pregunta', 'siguiente' u 'otra'.")
    
    def _contar_dato_curioso(self) -> None:
        """Cuenta un dato curioso sobre Cervantes."""
        dato = random.choice(self.datos_curiosos)
        print(f"Bot: 💡 {dato}")
        print("Bot: ¿Te gustó este dato? Puedo contarte más si quieres.")
    
    def _responder_emocion(self, mensaje: str) -> bool:
        """
        Responde a emociones detectadas en el mensaje.
        
        Args:
            mensaje: Mensaje del usuario
            
        Returns:
            True si se detectó y respondió a una emoción
        """
        for emocion, respuestas in RESPUESTAS_EMOCIONES.items():
            if emocion in mensaje:
                respuesta = random.choice(respuestas)
                print(f"Bot: {respuesta}")
                return True
        return False
    
    def _responder_interes(self, mensaje: str) -> bool:
        """
        Responde a intereses detectados en el mensaje.
        
        Args:
            mensaje: Mensaje del usuario
            
        Returns:
            True si se detectó y respondió a un interés
        """
        for interes, respuestas in RESPUESTAS_INTERESES.items():
            if interes in mensaje:
                respuesta = random.choice(respuestas)
                print(f"Bot: {respuesta}")
                return True
        return False
    
    def _responder_contexto(self, mensaje: str) -> bool:
        """
        Responde a temas relacionados con Cervantes detectados en el mensaje.
        
        Args:
            mensaje: Mensaje del usuario
            
        Returns:
            True si se detectó y respondió a un tema cervantino
        """
        for contexto, respuestas in RESPUESTAS_CONTEXTO.items():
            if contexto in mensaje:
                respuesta = random.choice(respuestas)
                print(f"Bot: {respuesta}")
                return True
        return False


def main():
    """Función principal."""
    try:
        chatbot = ChatbotCervantes()
        chatbot.iniciar_conversacion()
    except Exception as e:
        print(f"\n{ColoresCLI.ROJO}Error inesperado: {e}{ColoresCLI.RESET}")


if __name__ == "__main__":
    main()
