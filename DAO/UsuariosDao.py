import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Usuario
class UsuariosDao(dao):
    """
    Clase de objeto de acceso a datos de los usuarios
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[usuario.username,usuario.contraseña]
            cursor.callproc("crearUsuario",args)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False

    def consultar(self,username,contraseña):
        """
        Método encargado de consultar los datos de un usuario a partir de su correo y su contraseña.

        Parámetros:

        email -- que es el correo del usuario
        
        password -- que es la contraseña del usuario
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from usuarios where username='"+username+"' and contraseña=sha('"+contraseña+"');"
            cursor.execute(sql)
            usuario=None
            for row in cursor:
                username=row[0]
                contraseña=row[1]
                usuario=Usuario(username,contraseña)
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None