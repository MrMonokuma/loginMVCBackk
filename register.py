import mysql.connector
from mysql.connector import errorcode
from DAO.UsuariosDao import UsuariosDao
from DAO.models import Usuario
import json
import cgi
import os

print('Content-Type: text/json')
print('')

if os.environ['REQUEST_METHOD']=="POST":
    datos= cgi.FieldStorage()
    username=datos.getvalue('username')
    contraseña=datos.getvalue('contra')

    usuario=Usuario(username,contraseña)
    dao=UsuariosDao()
    if(dao.consultar(username,contraseña) is None):
        if(dao.registrar(usuario)):
            print(json.dumps('{"tipo":"OK","mensaje":"Usuario creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear usuario"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un usuario con esa identificación o con ese correo"}'))
