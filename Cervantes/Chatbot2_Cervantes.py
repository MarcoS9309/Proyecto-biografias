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

def saludo():
    saludos = [
        "🌞 ¡Bienvenido! Es un placer conversar contigo sobre Cervantes.",
        "📚 Hola, viajero curioso. ¿Listo para explorar la vida y obra de Cervantes?",
        "✨ Saludos. La literatura nos une, ¿te animas a responder una pregunta?"
    ]
    print("Bot:", random.choice(saludos))

def despedida():
    despedidas = [
        "🌙 Ha sido un gusto compartir este momento contigo. Que la curiosidad te acompañe siempre.",
        "📖 Gracias por tu interés. Recuerda que cada página leída es un paso hacia el conocimiento.",
        "🌟 Hasta pronto. Que la inspiración de Cervantes ilumine tu camino."
    ]
    print("Bot:", random.choice(despedidas))

def chatbot():
    saludo()
    while True:
        mensaje = input("Tú: ").strip().lower()
        if mensaje in ["adios", "hasta luego", "bye", "salir"]:
            despedida()
            break
        elif mensaje in ["pregunta", "siguiente", "otra"]:
            pregunta = obtener_pregunta()
            print(f"Bot: {pregunta['pregunta']}")
            for opcion in pregunta["opciones"]:
                print("  ", opcion)
            respuesta = input("Tu respuesta (a/b/c): ").strip().lower()
            if respuesta == pregunta["respuesta"]:
                comentarios = [
                    "🌿 ¡Excelente! Tu conocimiento florece como la prosa cervantina.",
                    "🎉 ¡Correcto! Has dado en el blanco, como un buen caballero andante.",
                    "👏 Muy bien, tu curiosidad te lleva lejos. ¿Te gustaría otra pregunta?"
                ]
                print("Bot:", random.choice(comentarios))
            else:
                comentarios = [
                    f"🌱 No te preocupes, aprender es un viaje. La respuesta era {pregunta['respuesta'].upper()}. ¿Intentamos otra?",
                    f"🔎 La opción correcta era {pregunta['respuesta'].upper()}. Cada error es una oportunidad para crecer.",
                    f"💡 Cervantes también aprendió de sus tropiezos. La respuesta era {pregunta['respuesta'].upper()}."
                ]
                print("Bot:", random.choice(comentarios))
            print("Bot: Si deseas continuar, escribe 'pregunta', 'siguiente' u 'otra'.")
        elif mensaje in ["hola", "buenas", "hey"]:
            saludo()
        else:
            print("Bot: Qué interesante tu mensaje. Si quieres una pregunta, escribe 'pregunta'. Si deseas despedirte, escribe 'adios'.")

if __name__ == "__main__":
    chatbot()