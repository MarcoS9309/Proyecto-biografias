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
        "🌞 ¡Bienvenido! Es un placer conversar contigo sobre Cervantes y sobre la vida misma.",
        "📚 Hola, viajero curioso. ¿Listo para explorar la obra de Cervantes o compartir tus pensamientos?",
        "✨ Saludos. La literatura nos une, pero también lo hacen los sueños y las emociones. ¿Cómo te encuentras hoy?"
    ]
    print("Bot:", random.choice(saludos))

def despedida():
    despedidas = [
        "🌙 Ha sido un gusto compartir este momento contigo. Recuerda que cada día es una nueva página por escribir.",
        "📖 Gracias por tu interés y tu compañía. Que la curiosidad y la esperanza te acompañen siempre.",
        "🌟 Hasta pronto. Que la inspiración de Cervantes y tu propia creatividad iluminen tu camino."
    ]
    print("Bot:", random.choice(despedidas))

def responder_emocion(mensaje):
    emociones = {
        "triste": "Siento que te sientas así. La literatura puede ser un refugio en momentos difíciles. Si quieres, puedo escucharte o proponerte una pregunta para distraerte.",
        "feliz": "¡Me alegra saberlo! Compartir alegría es tan importante como compartir conocimiento. ¿Te gustaría una pregunta sobre Cervantes o hablar de tus sueños?",
        "solo": "Aquí estoy para acompañarte. Cervantes también encontró compañía en sus personajes. ¿Quieres charlar, compartir algo o aprender juntos?",
        "aburrido": "¡Vamos a cambiar eso! ¿Te animas a una pregunta literaria, una curiosidad sobre Cervantes o prefieres hablar de tus intereses?",
        "cansado": "Descansar es importante. Si lo deseas, podemos conversar tranquilamente, compartir una reflexión o dejar la literatura para otro momento.",
        "ansioso": "La ansiedad es parte de la vida, pero también lo es la calma. Si quieres, podemos hablar de algo que te relaje o sumergirnos en una historia.",
        "soñador": "¡Qué bonito ser soñador! Cervantes también soñó con mundos imposibles. ¿Quieres compartir tus sueños o escuchar una historia inspiradora?"
    }
    for emocion, respuesta in emociones.items():
        if emocion in mensaje:
            print("Bot:", respuesta)
            return True
    return False

def responder_interes(mensaje):
    intereses = {
        "libro": "Los libros son puertas a otros mundos. ¿Tienes algún favorito o quieres saber más sobre los de Cervantes?",
        "arte": "El arte y la literatura siempre han ido de la mano. Cervantes admiraba la creatividad en todas sus formas. ¿Te gusta crear?",
        "historia": "La historia de Cervantes está llena de aventuras y aprendizajes. ¿Te gustaría una anécdota o compartir alguna historia personal?",
        "viaje": "Viajar en la imaginación es tan valioso como hacerlo en la realidad. ¿Te gustaría recorrer la España de Cervantes o hablar de tus propios viajes?",
        "amistad": "La amistad es uno de los tesoros de la vida. Cervantes valoraba mucho la compañía. ¿Quieres compartir algo sobre tus amigos?",
        "creatividad": "La creatividad nos permite transformar el mundo. ¿Hay algo creativo que te gustaría hacer o aprender?",
        "motivación": "A veces necesitamos palabras de ánimo. Recuerda: cada paso cuenta y cada error es una oportunidad. ¿Quieres hablar de tus metas?"
    }
    for interes, respuesta in intereses.items():
        if interes in mensaje:
            print("Bot:", respuesta)
            return True
    return False

def responder_contexto(mensaje):
    contexto = {
        "cervantes": "Miguel de Cervantes fue un hombre de sueños y luchas. Su vida estuvo marcada por la aventura, la creatividad y la perseverancia. ¿Te gustaría saber más sobre él?",
        "literatura": "La literatura nos permite comprender el mundo y a nosotros mismos. ¿Hay algún libro o autor que te inspire?",
        "quijote": "Don Quijote es el reflejo de la imaginación y la valentía. ¿Te identificas con algún personaje de la obra?",
        "españa": "La España de Cervantes era un lugar de contrastes y cambios. ¿Te gustaría viajar allí con la imaginación?"
    }
    for palabra, respuesta in contexto.items():
        if palabra in mensaje:
            print("Bot:", respuesta)
            return True
    return False

def responder_generico(mensaje):
    genericos = [
        "Me encanta conversar contigo. Si tienes dudas, sueños o curiosidades, aquí estoy para escucharte.",
        "La empatía es el puente entre las personas. ¿Quieres compartir cómo te sientes hoy o hablar de tus intereses?",
        "A veces, una buena charla puede iluminar el día. ¿Sobre qué te gustaría hablar? Puede ser literatura, emociones o cualquier tema.",
        "Recuerda que cada conversación es una oportunidad para aprender y crecer. ¿Te gustaría una pregunta, una reflexión o simplemente conversar?"
    ]
    print("Bot:", random.choice(genericos))

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
                    "👏 Muy bien, tu curiosidad te lleva lejos. ¿Te gustaría otra pregunta?",
                    "✨ Tu respuesta revela tu interés y pasión por aprender. ¡Sigue así!"
                ]
                print("Bot:", random.choice(comentarios))
            else:
                comentarios = [
                    f"🌱 No te preocupes, aprender es un viaje. La respuesta era {pregunta['respuesta'].upper()}. ¿Intentamos otra?",
                    f"🔎 La opción correcta era {pregunta['respuesta'].upper()}. Cada error es una oportunidad para crecer.",
                    f"💡 Cervantes también aprendió de sus tropiezos. La respuesta era {pregunta['respuesta'].upper()}.",
                    "🌻 Lo importante es intentarlo. ¿Quieres probar con otra pregunta o conversar sobre otro tema?"
                ]
                print("Bot:", random.choice(comentarios))
            print("Bot: Si deseas continuar, escribe 'pregunta', 'siguiente' u 'otra'.")
        elif mensaje in ["hola", "buenas", "hey"]:
            saludo()
        elif responder_emocion(mensaje):
            continue
        elif responder_interes(mensaje):
            continue
        elif responder_contexto(mensaje):
            continue
        else:
            responder_generico(mensaje)

if __name__ == "__main__":
    chatbot()