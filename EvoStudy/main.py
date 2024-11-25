import database
import estudiante
import docente
import ia
from form import form
import ollama


class forms:
    def __init__(self):
        self.Puntaje_Mate = 0
        self.Puntaje_Ciencia = 0
        self.Puntaje_Ing = 0
        self.Puntaje_No_Registrado = 0
        self.RunRevisionForm = False
        self.RunCrearForm = False
        self.Pais = "Costa Rica"

    def Revisar_Formulario(self, formulario):
        for materia in formulario:
            for pregunta in formulario[materia]:
                print("\n", pregunta)
                for letra in formulario[materia][pregunta]:
                    for respuestas in formulario[materia][pregunta][letra]:
                        print(letra + respuestas)
                self.RunRevisionForm = True
                while self.RunRevisionForm:
                    try:
                        respuesta = input()
                        for i in formulario[materia][pregunta][respuesta]:
                            for e in formulario[materia][pregunta][respuesta][i]:
                                if materia == "mate":
                                    self.Puntaje_Mate += int(e)
                                elif materia == "ciencias":
                                    self.Puntaje_Ciencia += int(e)
                                elif materia == "ingles":
                                    self.Puntaje_Ing += int(e)
                                else:
                                    self.Puntaje_No_Registrado += int(e)
                                self.RunRevisionForm = False
                    except:
                        print("Ha ocurrido un error. Ingrese de nuevo una opcion valida (a / b / c / d)")
        print("Puntaje de matematica: ", self.Puntaje_Mate)
        print("Puntaje de ciencias: ", self.Puntaje_Ciencia)
        print("Puntaje de ingles: ", self.Puntaje_Ing)
        if self.Puntaje_No_Registrado:
            print("Puntaje no registrado: ", self.Puntaje_No_Registrado)

    def Crear_Formulario(self):
        materiaForm = input("De que materia desea realizar el formulario?\n(mate / ciencias / ingles / otro) ")
        formulario = {materiaForm : {}}
        self.RunCrearForm = True
        while self.RunCrearForm:

            pregunta = input("Pregunta: \n")
            formulario[materiaForm][pregunta] = {}

            respuesta1 = input("Opcion a: ")
            formulario[materiaForm][pregunta]["a"] = {") " + respuesta1 : "0"}
            respuesta2 = input("Opcion b: ")
            formulario[materiaForm][pregunta]["b"] = {") " + respuesta2 : "0"}
            respuesta3 = input("Opcion c: ")
            formulario[materiaForm][pregunta]["c"] = {") " + respuesta3 : "0"}
            respuesta4 = input("Opcion d: ")
            formulario[materiaForm][pregunta]["d"] = {") " + respuesta4 : "0"}

            while True:
                respuestaCorrecta = input("Cual es la opcion correcta? (a / b / c / d): ")
                if respuestaCorrecta == "a":
                    formulario[materiaForm][pregunta]["a"] = {") " + respuesta1 : "1"}
                    break
                if respuestaCorrecta == "b":
                    formulario[materiaForm][pregunta]["b"] = {") " + respuesta2 : "1"}
                    break
                if respuestaCorrecta == "c":
                    formulario[materiaForm][pregunta]["c"] = {") " + respuesta3 : "1"}
                    break
                if respuestaCorrecta == "d":
                    formulario[materiaForm][pregunta]["d"] = {") " + respuesta4 : "1"}
                    break
                else:
                    print("Opcion no valida. Ingrese (a / b / c / d)")

            if input("Desea ingresar otra pregunta? (Y/N) ") == "N":
                self.RunCrearForm = False
        return formulario

    def Recomendar_Carrera(self):
        Pregunta = "Suponiendo que en un test de matematica, obtuve " + str(self.Puntaje_Mate) + " de 20, en uno de ciencias " + str(self.Puntaje_Ciencia) + " de 20 y en uno de ingles " + str(self.Puntaje_Ing) + " de 20, que carrera me recomendarias trabajar, y en que paginas podria estudiar esa carrera siendo de " + self.Pais + "?"
        Respuesta = ollama.chat(model=self.modelo, messages=[{"role": "user", "content": Pregunta}])
        print(Respuesta["message"]["content"])

    def Recomendar_Metas(self):
        Pregunta = "Suponiendo que en un test de matematica, obtuve " + str(self.Puntaje_Mate) + " de 20, en uno de ciencias " + str(self.Puntaje_Ciencia) + " de 20 y en uno de ingles " + str(self.Puntaje_Ing) + " de 20, que me recomendarias mejorar y proponerme como metas?"
        Respuesta = ollama.chat(model=self.modelo, messages=[{"role": "user", "content": Pregunta}])
        print(Respuesta["message"]["content"])


# Función para registrar un usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre: ").strip()
    contraseña = input("Ingrese su contraseña: ").strip()
    tipo_usuario = input("¿Es usted un 'estudiante' o 'docente'? ").lower().strip()

    if tipo_usuario not in ['estudiante', 'docente']:
        print("Rol no válido. Intente nuevamente.")
        return

    database.registrar_usuario(nombre, contraseña, tipo_usuario)
    print(f"Usuario {tipo_usuario} registrado exitosamente.")

# Función para iniciar sesión
def iniciar_sesion():
    exito, nombre, tipo_usuario = database.iniciar_sesion()

    if not exito:
        return

    print(f"Bienvenido, {nombre} ({tipo_usuario.capitalize()})!")

    if tipo_usuario == 'estudiante':
        menu_estudiante(nombre)
    elif tipo_usuario == 'docente':
        menu_docente(nombre)

# Menú para el estudiante
def menu_estudiante(estudiante_id):
    while True:
        print("\n1. Consultar materias pendientes")
        print("2. Consultar con la IA")
        print("3. Realizar formulario")
        print("4. Recomenda carrera")
        print("5. Recomendar metas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            materias = estudiante.consultar_materias(estudiante_id)
            print("Materias pendientes:", ", ".join(materias))
        elif opcion == '2':
            pregunta = input("¿Qué te gustaría preguntar a la IA? ").strip()
            respuesta = ia.obtener_respuesta_ia(pregunta)
            print("Respuesta de la IA:", respuesta)
        elif opcion == '3':
            formularios.Revisar_Formulario(form)
        elif opcion == '4':
            formularios.Recomendar_Carrera()
        elif opcion == '5':
            formularios.Recomendar_Metas()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Menú para el docente
def menu_docente(docente_id):
    while True:
        print("\n1. Crear tarea")
        print("2. Crear equipo")
        print("3. Consultar con la IA")
        print("4. Enviar mensaje a un estudiante")
        print("5. Crear formulario")
        print("6. Probar formulario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ").strip()
            docente.crear_tarea(docente_id, descripcion)
            print("Tarea creada exitosamente.")
        elif opcion == '2':
            nombre_equipo = input("Ingrese el nombre del equipo: ").strip()
            estudiantes = input("Ingrese los nombres de los estudiantes (separados por coma): ").split(',')
            docente.crear_equipo(docente_id, nombre_equipo, estudiantes)
            print("Equipo creado exitosamente.")
        elif opcion == '3':
            pregunta = input("¿Qué te gustaría preguntar a la IA? ").strip()
            respuesta = ia.obtener_respuesta_ia(pregunta)
            print("Respuesta de la IA:", respuesta)
        elif opcion == '4':
            estudiante_id = input("Ingrese el ID del estudiante: ").strip()
            mensaje = input("Ingrese el mensaje a enviar: ").strip()
            docente.enviar_mensaje(docente_id, estudiante_id, mensaje)
            print("Mensaje enviado exitosamente.")
        elif opcion == '5':
            formulario_personalizado = formularios.Crear_Formulario()
        elif opcion == '6':
            Formulario = int(input("Desea probar un formulario propio (0) o uno prehecho (1)"))
            if Formulario == 0:
                try:
                    formularios.Revisar_Formulario(formulario_personalizado)
                except:
                    print("No hay ningun formulario creado")
            elif Formulario == 1:
                formularios.Revisar_Formulario(form)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Programa principal
if __name__ == "__main__":
    database.inicializar_base_datos()
    formularios = forms()

    while True:
        print("\n1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

