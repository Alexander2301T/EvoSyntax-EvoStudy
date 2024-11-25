import sqlite3

# Inicializar la base de datos y las tablas
def inicializar_base_datos():
    conexion = sqlite3.connect("sistema_escolar.db")
    cursor = conexion.cursor()

    # Crear tabla de usuarios
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        contraseña TEXT NOT NULL,
                        tipo_usuario TEXT NOT NULL
                    )''')
    # Crear tabla de tareas
    cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        docente TEXT NOT NULL,
                        descripcion TEXT NOT NULL
                    )''')
    # Crear tabla de equipos
    cursor.execute('''CREATE TABLE IF NOT EXISTS equipos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_equipo TEXT NOT NULL,
                        estudiantes TEXT NOT NULL
                    )''')

    conexion.commit()
    conexion.close()

# Registrar usuario
def registrar_usuario(nombre, contraseña, tipo_usuario):
    conexion = sqlite3.connect("sistema_escolar.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, contraseña, tipo_usuario) VALUES (?, ?, ?)",
                    (nombre, contraseña, tipo_usuario))
    conexion.commit()
    conexion.close()

# Iniciar sesión
def iniciar_sesion():
    conexion = sqlite3.connect("sistema_escolar.db")
    cursor = conexion.cursor()

    nombre = input("Ingresa tu nombre de usuario: ").strip()
    contraseña = input("Ingresa tu contraseña: ").strip()

    cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND contraseña = ?", (nombre, contraseña))
    usuario = cursor.fetchone()

    conexion.close()

    if usuario:
        return True, nombre, usuario[3]
    else:
        print("[ERROR] Usuario o contraseña incorrectos.")
        return False, None, None


