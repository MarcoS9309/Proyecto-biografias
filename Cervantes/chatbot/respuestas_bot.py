"""
Respuestas y configuraciones para el chatbot de Cervantes.
Contiene todos los textos, emociones e intereses que puede manejar el bot.
"""

import random

# Saludos del chatbot
SALUDOS = [
    "🌞 ¡Bienvenido! Es un placer conversar contigo sobre Cervantes y sobre la vida misma.",
    "📚 Hola, viajero curioso. ¿Listo para explorar la obra de Cervantes o compartir tus pensamientos?",
    "✨ Saludos. La literatura nos une, pero también lo hacen los sueños y las emociones. ¿Cómo te encuentras hoy?",
    "🌟 ¡Hola! Soy tu compañero en este viaje por el mundo cervantino. ¿Qué te trae por aquí?"
]

# Despedidas del chatbot
DESPEDIDAS = [
    "🌙 Ha sido un gusto compartir este momento contigo. Recuerda que cada día es una nueva página por escribir.",
    "📖 Gracias por tu interés y tu compañía. Que la curiosidad y la esperanza te acompañen siempre.",
    "🌟 Hasta pronto. Que la inspiración de Cervantes y tu propia creatividad iluminen tu camino.",
    "💫 Me alegra haber conversado contigo. ¡Que tengas un día lleno de descubrimientos!"
]

# Respuestas a emociones
RESPUESTAS_EMOCIONES = {
    "triste": [
        "Siento que te sientas así. La literatura puede ser un refugio en momentos difíciles. Si quieres, puedo escucharte o proponerte una pregunta para distraerte.",
        "Comprendo tu tristeza. A veces, las palabras de Cervantes pueden ofrecer consuelo. ¿Te gustaría compartir lo que sientes?"
    ],
    "feliz": [
        "¡Me alegra saberlo! Compartir alegría es tan importante como compartir conocimiento. ¿Te gustaría una pregunta sobre Cervantes o hablar de tus sueños?",
        "¡Qué maravilloso! La felicidad es contagiosa. ¿Quieres celebrar aprendiendo algo nuevo?"
    ],
    "solo": [
        "Aquí estoy para acompañarte. Cervantes también encontró compañía en sus personajes. ¿Quieres charlar, compartir algo o aprender juntos?",
        "No estás solo/a. La literatura es una forma hermosa de conectar con otros. ¿Te animas a una conversación?"
    ],
    "aburrido": [
        "¡Vamos a cambiar eso! ¿Te animas a una pregunta literaria, una curiosidad sobre Cervantes o prefieres hablar de tus intereses?",
        "El aburrimiento puede ser el inicio de una aventura. ¿Qué tal si exploramos juntos el mundo de Cervantes?"
    ],
    "cansado": [
        "Descansar es importante. Si lo deseas, podemos conversar tranquilamente, compartir una reflexión o dejar la literatura para otro momento.",
        "Comprendo el cansancio. A veces, una charla relajada puede ser reconfortante."
    ],
    "ansioso": [
        "La ansiedad es parte de la vida, pero también lo es la calma. Si quieres, podemos hablar de algo que te relaje o sumergirnos en una historia.",
        "Entiendo esa sensación. La literatura puede ser un bálsamo para el alma inquieta."
    ],
    "soñador": [
        "¡Qué bonito ser soñador! Cervantes también soñó con mundos imposibles. ¿Quieres compartir tus sueños o escuchar una historia inspiradora?",
        "Los sueños dan sentido a la vida. Cervantes fue un gran soñador. ¿Cuáles son tus sueños?"
    ]
}

# Respuestas a intereses
RESPUESTAS_INTERESES = {
    "libro": [
        "Los libros son puertas a otros mundos. ¿Tienes algún favorito o quieres saber más sobre los de Cervantes?",
        "¡Maravilloso! La lectura enriquece el alma. ¿Qué tipo de libros te apasionan?"
    ],
    "arte": [
        "El arte y la literatura siempre han ido de la mano. Cervantes admiraba la creatividad en todas sus formas. ¿Te gusta crear?",
        "El arte es expresión pura. Cervantes veía la escritura como un arte supremo."
    ],
    "historia": [
        "La historia de Cervantes está llena de aventuras y aprendizajes. ¿Te gustaría una anécdota o compartir alguna historia personal?",
        "La historia nos enseña y nos inspira. Cervantes vivió una época fascinante."
    ],
    "viaje": [
        "Viajar en la imaginación es tan valioso como hacerlo en la realidad. ¿Te gustaría recorrer la España de Cervantes o hablar de tus propios viajes?",
        "Los viajes transforman el alma. Cervantes viajó mucho, física y mentalmente."
    ],
    "amistad": [
        "La amistad es uno de los tesoros de la vida. Cervantes valoraba mucho la compañía. ¿Quieres compartir algo sobre tus amigos?",
        "La amistad verdadera es un regalo. ¿Tienes amigos que compartan tu amor por la literatura?"
    ],
    "creatividad": [
        "La creatividad nos permite transformar el mundo. ¿Hay algo creativo que te gustaría hacer o aprender?",
        "¡Qué hermoso impulso! La creatividad es la chispa divina que todos llevamos dentro."
    ],
    "motivación": [
        "A veces necesitamos palabras de ánimo. Recuerda: cada paso cuenta y cada error es una oportunidad. ¿Quieres hablar de tus metas?",
        "La motivación viene del corazón. ¿Qué te inspira a seguir adelante?"
    ]
}

# Respuestas sobre contexto cervantino
RESPUESTAS_CONTEXTO = {
    "cervantes": [
        "Miguel de Cervantes fue un hombre de sueños y luchas. Su vida estuvo marcada por la aventura, la creatividad y la perseverancia. ¿Te gustaría saber más sobre él?",
        "Cervantes representa el espíritu indomable del ser humano. ¿Qué aspecto de su vida te resulta más interesante?"
    ],
    "literatura": [
        "La literatura nos permite comprender el mundo y a nosotros mismos. ¿Hay algún libro o autor que te inspire?",
        "La literatura es el espejo del alma humana. ¿Qué te atrae más de ella?"
    ],
    "quijote": [
        "Don Quijote es el reflejo de la imaginación y la valentía. ¿Te identificas con algún personaje de la obra?",
        "El Quijote nos enseña sobre los sueños y la realidad. ¿Cuál es tu personaje favorito?"
    ],
    "españa": [
        "La España de Cervantes era un lugar de contrastes y cambios. ¿Te gustaría viajar allí con la imaginación?",
        "España en tiempos de Cervantes era fascinante. ¿Conoces algo sobre esa época?"
    ]
}

# Respuestas genéricas
RESPUESTAS_GENERICAS = [
    "Me encanta conversar contigo. Si tienes dudas, sueños o curiosidades, aquí estoy para escucharte.",
    "La empatía es el puente entre las personas. ¿Quieres compartir cómo te sientes hoy o hablar de tus intereses?",
    "A veces, una buena charla puede iluminar el día. ¿Sobre qué te gustaría hablar? Puede ser literatura, emociones o cualquier tema.",
    "Recuerda que cada conversación es una oportunidad para aprender y crecer. ¿Te gustaría una pregunta, una reflexión o simplemente conversar?",
    "La vida es como un libro abierto. ¿Qué página te gustaría escribir hoy?",
    "Cada persona tiene una historia única. ¿Te animas a compartir la tuya?"
]

# Comentarios para respuestas correctas
COMENTARIOS_CORRECTO = [
    "🌿 ¡Excelente! Tu conocimiento florece como la prosa cervantina.",
    "🎉 ¡Correcto! Has dado en el blanco, como un buen caballero andante.",
    "👏 Muy bien, tu curiosidad te lleva lejos. ¿Te gustaría otra pregunta?",
    "✨ Tu respuesta revela tu interés y pasión por aprender. ¡Sigue así!",
    "🌟 ¡Perfecto! Cervantes estaría orgulloso de tu conocimiento.",
    "🏆 ¡Magistral! Tu respuesta demuestra verdadera comprensión."
]

# Comentarios para respuestas incorrectas
COMENTARIOS_INCORRECTO = [
    "🌱 No te preocupes, aprender es un viaje. La respuesta era {respuesta}. ¿Intentamos otra?",
    "🔎 La opción correcta era {respuesta}. Cada error es una oportunidad para crecer.",
    "💡 Cervantes también aprendió de sus tropiezos. La respuesta era {respuesta}.",
    "🌻 Lo importante es intentarlo. La respuesta correcta era {respuesta}. ¿Quieres probar con otra pregunta?",
    "🎯 Cerca, pero no del todo. La respuesta era {respuesta}. ¡Sigamos aprendiendo!",
    "🌈 Cada error nos acerca al conocimiento. La respuesta era {respuesta}."
]


def obtener_saludo() -> str:
    """Retorna un saludo aleatorio."""
    return random.choice(SALUDOS)


def obtener_despedida() -> str:
    """Retorna una despedida aleatoria."""
    return random.choice(DESPEDIDAS)


def obtener_comentario_correcto() -> str:
    """Retorna un comentario aleatorio para respuesta correcta."""
    return random.choice(COMENTARIOS_CORRECTO)


def obtener_comentario_incorrecto(respuesta_correcta: str) -> str:
    """Retorna un comentario aleatorio para respuesta incorrecta."""
    comentario = random.choice(COMENTARIOS_INCORRECTO)
    return comentario.format(respuesta=respuesta_correcta.upper())


def obtener_respuesta_generica() -> str:
    """Retorna una respuesta genérica aleatoria."""
    return random.choice(RESPUESTAS_GENERICAS)
