from logger_base import log
from usuario_dao import UsuarioDAO
from conexion import Conexion
from usuario import Usuario
from cursor_del_pool import CursorDelPool

salir = False
while not salir:
    print('''Opciones:
        1. Listar usuarios
        2. Agregar usuario
        3. Modificar usuario
        4. Eliminar usuario
        5. salir''')
    opcion = int(input('Escribe tu opcion (1-5):'))
    if opcion == 1:
        listado_usuarios = UsuarioDAO.seleccionar()
        for usuario in listado_usuarios:
            log.debug(usuario)
    elif opcion == 2:
        username = input('Escribe el username: ')
        password = input('Escribe el password: ')
        nuevo_usuario = Usuario(username=username, password=password)
        insertar_usuario = UsuarioDAO.insertar(nuevo_usuario)
        log.debug(insertar_usuario)
    elif opcion == 3:
        id_usuario = int(input('Escribe el id usuario a modificar: '))
        username_mod = input('Escribe el nuevo username: ')
        password_mod = input('Escribe el nuevo password: ')
        usuario_mod = Usuario(id_usuario=id_usuario, username=username_mod, password=password_mod)
        nuevo_usuario_modificado = UsuarioDAO.actualizar(usuario_mod)
        log.debug(nuevo_usuario_modificado)
    elif opcion == 4:
        id_usuario = int(input('Escribe el id_usuario a eliminar: '))
        usuario_eliminar = Usuario(id_usuario=id_usuario)
        usuario_eliminado = UsuarioDAO.eliminar(usuario_eliminar)
        log.debug(usuario_eliminado)
    elif opcion == 5:
        salir = True
        print('Saliendo del menú...')
    else:
        print('Ocurrio un error...')