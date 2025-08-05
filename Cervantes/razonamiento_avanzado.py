import random

def modo_desafio_cervantes():
    print("""
    =============================================
    MODO DESAFÍO: CERVANTES
    ¡Pon a prueba tu conocimiento avanzado!
    =============================================
    """)

    preguntas_desafio = [
        {
            "pregunta": "¿Qué pseudónimo usó Cervantes en algunos de sus escritos?",
            "opciones": ["a) El Manco de Lepanto", "b) Mateo Alemán", "c) Saavedra"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Cuál fue la primera obra publicada por Cervantes?",
            "opciones": ["a) La Galatea", "b) El Quijote", "c) Novelas Ejemplares"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿En qué año se publicó la segunda parte de Don Quijote?",
            "opciones": ["a) 1605", "b) 1615", "c) 1620"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué personaje de Don Quijote representa la cordura frente a la locura?",
            "opciones": ["a) Sancho Panza", "b) Dulcinea", "c) El cura"],
            "respuesta": "a"
        },
        {
            "pregunta": "¿Dónde murió Cervantes?",
            "opciones": ["a) Madrid", "b) Sevilla", "c) Alcalá de Henares"],
            "respuesta": "a"
        }
    ]

    random.shuffle(preguntas_desafio)
    puntaje = 0
    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas_desafio):
        print(f"\nDesafío {i+1}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(f"  {opcion}")
        respuesta = input("Tu respuesta (a/b/c): ").strip().lower()
        respuestas_usuario.append(respuesta)
        if respuesta == pregunta["respuesta"]:
            puntaje += 1
            print("🌟 ¡Correcto!\n")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {pregunta['respuesta'].upper()}\n")

    print("\n" + "="*50)
    print(f"PUNTAJE FINAL DESAFÍO: {puntaje}/{len(preguntas_desafio)}")
    if puntaje == len(preguntas_desafio):
        print("🏆 ¡Eres un cervantista experto!")
    elif puntaje >= len(preguntas_desafio)//2:
        print("🔎 Buen trabajo, pero Cervantes aún guarda secretos para ti.")
    else:
        print("📚 ¡Ánimo! La lectura te hará maestro.")

    print("\nDato curioso:")
    print("¿Sabías que Cervantes y Shakespeare murieron en 1616, pero en días distintos y bajo calendarios diferentes?")

if __name__ == "__main__":
    modo_desafio_cervantes()