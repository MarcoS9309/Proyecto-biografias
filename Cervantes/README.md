# Sistema Cervantino Interactivo 📚

Un sistema educativo interactivo dedicado a Miguel de Cervantes, el gran escritor español autor de *Don Quijote de la Mancha*.

## 🌟 Características

- **Evaluación Básica**: Test de conocimientos fundamentales sobre la vida y obra de Cervantes
- **Modo Desafío**: Preguntas avanzadas con orden aleatorio para expertos cervantinos
- **Chatbot Interactivo**: Conversación empática sobre literatura, emociones y temas generales
- **Interfaz Colorida**: Terminal con colores y emojis para una experiencia visual atractiva
- **Retroalimentación Educativa**: Comentarios personalizados y datos curiosos

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7 o superior
- Terminal compatible con códigos de color ANSI

### Ejecución
```bash
cd Cervantes
python main.py
```

## 📁 Estructura del Proyecto

```
Cervantes/
├── main.py                    # Punto de entrada principal
├── data/                      # Datos del proyecto
│   ├── __init__.py
│   └── preguntas_cervantes.py # Preguntas y datos curiosos
├── utils/                     # Utilidades comunes
│   ├── __init__.py
│   └── utilidades.py          # Funciones de apoyo y colores
├── evaluadores/               # Módulos de evaluación
│   ├── __init__.py
│   ├── evaluador_basico.py    # Evaluación básica
│   └── evaluador_avanzado.py  # Modo desafío
├── chatbot/                   # Sistema de chatbot
│   ├── __init__.py
│   ├── chatbot_principal.py   # Chatbot principal
│   └── respuestas_bot.py      # Respuestas y configuración
└── README.md                  # Este archivo
```

## 🎯 Funcionalidades

### 1. Evaluación Básica
- 6 preguntas sobre aspectos fundamentales de Cervantes
- Retroalimentación específica para cada respuesta incorrecta
- Sistema de calificación con mensajes motivacionales
- Datos curiosos al final de la evaluación

### 2. Modo Desafío (Evaluación Avanzada)
- 5 preguntas de nivel avanzado
- Orden aleatorio para mayor desafío
- Calificaciones específicas para expertos
- Retroalimentación avanzada según el rendimiento

### 3. Chatbot Interactivo
- Respuestas empáticas a emociones (tristeza, felicidad, soledad, etc.)
- Conversación sobre intereses (libros, arte, historia, etc.)
- Información contextual sobre Cervantes y su obra
- Preguntas interactivas durante la conversación
- Datos curiosos bajo demanda

## 🎨 Características Técnicas

### Arquitectura Modular
- **Separación de responsabilidades**: Cada módulo tiene una función específica
- **Reutilización de código**: Funciones comunes centralizadas en `utils`
- **Fácil mantenimiento**: Estructura clara y documentada
- **Extensibilidad**: Fácil agregar nuevas preguntas o funcionalidades

### Manejo de Errores
- Captura de interrupciones del usuario (Ctrl+C)
- Validación de entradas
- Mensajes de error informativos
- Recuperación elegante de errores

### Experiencia de Usuario
- Colores y emojis para mayor atractivo visual
- Mensajes personalizados y variados
- Navegación intuitiva
- Retroalimentación inmediata

## 📖 Ejemplos de Uso

### Ejecutar Evaluación Básica
```bash
# Desde el directorio Cervantes
python evaluadores/evaluador_basico.py
```

### Ejecutar Modo Desafío
```bash
# Desde el directorio Cervantes
python evaluadores/evaluador_avanzado.py
```

### Ejecutar Solo el Chatbot
```bash
# Desde el directorio Cervantes
python chatbot/chatbot_principal.py
```

## 🔧 Personalización

### Agregar Nuevas Preguntas
Edita `data/preguntas_cervantes.py` y agrega preguntas en el formato:
```python
{
    "pregunta": "Tu pregunta aquí",
    "opciones": ["a) Opción 1", "b) Opción 2", "c) Opción 3"],
    "respuesta": "a",
    "retroalimentacion": "Explicación educativa"
}
```

### Modificar Respuestas del Chatbot
Edita `chatbot/respuestas_bot.py` para personalizar:
- Saludos y despedidas
- Respuestas a emociones
- Comentarios para respuestas correctas/incorrectas
- Respuestas genéricas

### Personalizar Colores
Modifica la clase `ColoresCLI` en `utils/utilidades.py` para cambiar los colores de la terminal.

## 🎓 Objetivo Educativo

Este proyecto tiene como objetivo:
- Fomentar el aprendizaje sobre Miguel de Cervantes
- Hacer la educación más interactiva y divertida
- Desarrollar empatía a través de la conversación
- Promover el amor por la literatura española

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:
- Agregar más preguntas sobre Cervantes
- Mejorar las respuestas del chatbot
- Añadir nuevas funcionalidades
- Mejorar la documentación

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🙏 Agradecimientos

- A Miguel de Cervantes por su legado literario
- A todos los educadores que inspiran el amor por la literatura
- A la comunidad de Python por las herramientas que hacen posible este proyecto

---

*"La pluma es lengua del alma"* - Miguel de Cervantes
