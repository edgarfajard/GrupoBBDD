import mysql.connector
from mysql.connector import Error

#Tengo problemas con el pip, no me reconoce elmysql.connector, problema a arreglar#

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123456',
                db='universidad2'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))
