import database
import ia

# Función para crear una tarea
def crear_tarea(docente_id, descripcion):
    database.crear_tarea(docente_id, descripcion)

# Función para crear un equipo
def crear_equipo(docente_id, nombre_equipo, estudiantes):
    database.crear_equipo(docente_id, nombre_equipo, estudiantes)

# Función para hacer una consulta a la IA del docente
def consultar_ia(pregunta):
    return ia.consultar_ia_docente(pregunta)

# Función para enviar un mensaje a un estudiante
def enviar_mensaje(docente_id, estudiante_id, mensaje):
    database.enviar_mensaje(docente_id, estudiante_id, mensaje)
