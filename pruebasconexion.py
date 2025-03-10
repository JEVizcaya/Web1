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
        #consulta = "SELECT * FROM actor"
        #ejecutamos consulta
        #cursor.execute(consulta)
        #obtenemos los datos
        #actores = cursor.fetchall()
        #recorremos los datos
        #for actor in actores:
            #print(actor)
            # Datos a insertar
        first_name = 'Jane'
        last_name = 'Smith'

        # Consulta SQL para insertar un nuevo actor
        consulta = "INSERT INTO actor (first_name, last_name) VALUES (%s, %s)"
        
        # Ejecutamos la consulta pasando los parámetros
        cursor.execute(consulta, (first_name, last_name))

        # Confirmamos los cambios en la base de datos
        conexion.commit()

        print("Nuevo actor insertado exitosamente")
except Exception as e:
    print("Ocurrió un error al consultar: ", e)
            
finally:
    conexion.close()
    print("Conexión cerrada")
    