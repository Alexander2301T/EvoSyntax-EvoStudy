import database
import ia

# Función para consultar las materias pendientes de un estudiante
def consultar_materias(id_estudiante):
    return database.consultar_materias_pendientes(id_estudiante)

# Función para hacer una consulta a la IA del estudiante
def consultar_ia(pregunta):
    return ia.consultar_ia_estudiante(pregunta)


