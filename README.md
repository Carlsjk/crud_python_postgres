# Proyecto de Gestión de Usuarios

Este es un proyecto de gestión de usuarios utilizando patrones de diseño DAO (Data Access Object) con la implementación de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para interactuar con una base de datos.

## Requisitos

- Python 3.x
- PostgreSQL
- Librerías de Python:
  - `psycopg2` para interactuar con PostgreSQL
  - `logging` para gestionar los logs
  - `cursor_del_pool` para el manejo de conexiones a la base de datos mediante un pool de conexiones.

## Descripción

Este proyecto tiene como objetivo realizar operaciones básicas sobre una tabla `usuarios` en una base de datos PostgreSQL. Las operaciones incluyen:
- **Listar usuarios**.
- **Agregar usuarios**.
- **Modificar usuarios**.
- **Eliminar usuarios**.

Cada acción está representada por una opción en un menú interactivo.

## Archivos principales

1. **`usuario.py`**: Define la clase `Usuario`, que representa un usuario con atributos como `id_usuario`, `username` y `password`. Contiene métodos getter y setter para estos atributos.
2. **`usuario_dao.py`**: Implementa la clase `UsuarioDAO` con métodos estáticos para realizar operaciones CRUD sobre la base de datos.
3. **`conexion.py`**: Establece la conexión con la base de datos PostgreSQL.
4. **`cursor_del_pool.py`**: Administra la conexión a la base de datos utilizando un pool de conexiones.
5. **`logger_base.py`**: Configura el sistema de logging para registrar información detallada de las operaciones realizadas.

## Instalación

1. Clona este repositorio en tu máquina local.

   ```bash
   git clone <URL del repositorio>
Instala las dependencias necesarias.

bash
Copiar
Editar
pip install psycopg2
Configura la conexión a tu base de datos en el archivo conexion.py:

python
Copiar
Editar
# Datos de conexión
DATABASE = 'nombre_de_base_de_datos'
USER = 'usuario_de_base_de_datos'
PASSWORD = 'contraseña'
HOST = 'localhost'
PORT = '5432'
Uso
Ejecuta el archivo principal para acceder al menú interactivo.

bash
Copiar
Editar
python main.py
El menú ofrecerá las siguientes opciones:

1: Listar todos los usuarios.
2: Agregar un nuevo usuario.
3: Modificar un usuario existente.
4: Eliminar un usuario.
5: Salir del programa.
Los logs se guardarán en un archivo llamado laboratorio_usuarios.log.

Ejemplo de operaciones
Listar usuarios:
bash
Copiar
Editar
1. Listar usuarios
Agregar usuario:
bash
Copiar
Editar
2. Agregar usuario
Escribe el username: jperez
Escribe el password: 123
Modificar usuario:
bash
Copiar
Editar
3. Modificar usuario
Escribe el id usuario a modificar: 1
Escribe el nuevo username: jramirez
Escribe el nuevo password: 852
Eliminar usuario:
bash
Copiar
Editar
4. Eliminar usuario
Escribe el id_usuario a eliminar: 2