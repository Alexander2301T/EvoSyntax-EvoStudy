import ollama

# Función para interactuar con la IA
def obtener_respuesta_ia(pregunta):
    respuesta = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": pregunta}])
    return respuesta["message"]["content"]

# Función para que el estudiante consulte a la IA
def consultar_ia_estudiante(pregunta):
    return obtener_respuesta_ia(pregunta)

# Función para que el docente consulte a la IA
def consultar_ia_docente(pregunta):
    return obtener_respuesta_ia(pregunta)
