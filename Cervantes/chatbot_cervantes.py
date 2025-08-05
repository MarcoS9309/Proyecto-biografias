import random

def obtener_pregunta():
    preguntas = [
        {
            "pregunta": "¿Qué pseudónimo usó Cervantes en algunos de sus escritos?",
            "opciones": ["a) El Manco de Lepanto", "b) Mateo Alemán", "c) Saavedra"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Cuál fue la primera obra publicada por Cervantes?",
            "opciones": ["a) La Galatea", "b) El Quijote", "c) Novelas Ejemplares"],
            "respuesta": "a"
        }
    ]
    return random.choice(preguntas)

def chatbot():
    print("👋 ¡Hola! Soy el mini-chatbot de Cervantes. Escribe 'pregunta' para responder una pregunta, 'adios' para salir.")
    while True:
        mensaje = input("Tú: ").strip().lower()
        if mensaje == "adios":
            print("Bot: ¡Hasta pronto! Sigue aprendiendo sobre Cervantes.")
            break
        elif mensaje == "pregunta":
            pregunta = obtener_pregunta()
            print("Bot:", pregunta["pregunta"])
            for opcion in pregunta["opciones"]:
                print("  ", opcion)
            respuesta = input("Tu respuesta (a/b/c): ").strip().lower()
            if respuesta == pregunta["respuesta"]:
                print("Bot: ¡Correcto! ¿Quieres otra pregunta? Escribe 'pregunta'.")
            else:
                print(f"Bot: Incorrecto. La respuesta era {pregunta['respuesta'].upper()}. Escribe 'pregunta' para intentar otra.")
        else:
            print("Bot: No entiendo. Escribe 'pregunta' para jugar o 'adios' para salir.")

if __name__ == "__main__":
    chatbot()