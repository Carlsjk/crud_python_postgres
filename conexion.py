from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5434'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MAX_CON, cls._MAX_CON,
                                                    host=cls._HOST,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    port=cls._DB_PORT,
                                                    database=cls._DATABASE)
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        try:
            conexion = cls.obtenerPool().getconn()
            return conexion
        except Exception as e:
            log.debug(f'Ocurrio un error: {e}')

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
    
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
    



    
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
