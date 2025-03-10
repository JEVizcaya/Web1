#importamos pymysql
import pymysql
#creamos conexion
conexion = pymysql.connect(
                            host='localhost',
                            user='root',
                            password='',
                            db='sakila')

try:
    with conexion.cursor() as cursor:
        #creamos consulta
        consulta = "SELECT * FROM actor"
        #ejecutamos consulta
        cursor.execute(consulta)
        #obtenemos los datos
        actores = cursor.fetchall()
        #recorremos los datos
        for actor in actores:
            print(actor)
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
            
finally:
    conexion.close()
    print("Conexión cerrada")
    