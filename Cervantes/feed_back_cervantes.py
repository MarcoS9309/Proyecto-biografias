def test_biografia_cervantes():
    print("""
    =============================================
    EVALUACIÓN DE CONOCIMIENTOS SOBRE CERVANTES
    =============================================
    """)
    
    preguntas = [
        {
            "pregunta": "1. ¿En qué batalla participó Cervantes donde perdió la movilidad de su mano izquierda?",
            "opciones": ["a) Batalla de Pavía", "b) Batalla de Lepanto", "c) Batalla de San Quintín"],
            "respuesta": "b"
        },
        {
            "pregunta": "2. ¿Cuántos años permaneció cautivo en Argel?",
            "opciones": ["a) 3 años", "b) 5 años", "c) 7 años"],
            "respuesta": "b"
        },
        {
            "pregunta": "3. ¿Qué obra es considerada la primera novela moderna según la biografía?",
            "opciones": ["a) La Galatea", "b) Novelas Ejemplares", "c) Don Quijote de la Mancha"],
            "respuesta": "c"
        },
        {
            "pregunta": "4. Según la cita presentada, ¿qué representa 'la pluma' para Cervantes?",
            "opciones": ["a) Un instrumento de poder", "b) Lengua del alma", "c) Herramienta de libertad"],
            "respuesta": "b"
        },
        {
            "pregunta": "5. ¿Qué aspecto destaca la crítica contemporánea mencionada en la biografía?",
            "opciones": ["a) Su uso de la métrica poética", "b) Maestría en caracterización psicológica", "c) Innovación en teatro clásico"],
            "respuesta": "b"
        },
        {
            "pregunta": "6. ¿Qué obra cervantina explora 'los laberintos de la condición humana' según el texto?",
            "opciones": ["a) Los trabajos de Persiles y Sigismunda", "b) Novelas Ejemplares", "c) La Numancia"],
            "respuesta": "b"
        }
    ]

    puntaje = 0
    respuestas_usuario = []

    for i, pregunta in enumerate(preguntas):
        print(pregunta["pregunta"])
        for opcion in pregunta["opciones"]:
            print(f"  {opcion}")
        
        respuesta = input("Tu respuesta (a/b/c): ").strip().lower()
        respuestas_usuario.append(respuesta)
        
        if respuesta == pregunta["respuesta"]:
            puntaje += 1
            print("✓ Correcto\n")
        else:
            print(f"✗ Incorrecto. La respuesta correcta es: {pregunta['respuesta'].upper()}\n")

    # Resultado final
    print("\n" + "="*50)
    print(f"PUNTAJE FINAL: {puntaje}/{len(preguntas)}")
    
    if puntaje == len(preguntas):
        print("¡Excelente! Dominas la biografía cervantina")
    elif puntaje >= len(preguntas)//2:
        print("Buen conocimiento, pero puedes mejorar algunos detalles")
    else:
        print("Revisa la biografía con más atención")
    
    # Retroalimentación específica
    print("\nRETROALIMENTACIÓN:")
    retro = {
        0: "Revisa el contexto histórico de Cervantes y su participación militar",
        1: "El cautiverio argelino fue crucial en su vida (1575-1580)",
        2: "El Quijote revolucionó la narrativa occidental",
        3: "Cervantes valoraba la escritura como expresión del alma",
        4: "Los estudiosos destacan su profundidad psicológica",
        5: "Las Novelas Ejemplares son joyas del relato breve"
    }
    
    for i, (preg, resp_usuario) in enumerate(zip(preguntas, respuestas_usuario)):
        if resp_usuario != preg["respuesta"]:
            print(f"- Pregunta {i+1}: {retro[i]}")

if __name__ == "__main__":
    test_biografia_cervantes()