import psycopg2 as db

conexion= db.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test_db'
)


try:
       with conexion:
           with conexion.cursor() as cursor:
                       cursor=conexion.cursor()
                       sentencia='INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
                       valores=('Maria','Alvarez','maria@gmail.com')
                       cursor.execute(sentencia, valores)

                       sentencia = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
                       valores=('juanito0000000000','juanito','juanito.gmail',7)
                       cursor.execute(sentencia, valores)
           conexion.commit()



except Exception as e:
    conexion.rollback()
    print(f'Ocurrio errror se hizo rollback: {e}')
finally:
     conexion.close()

print('Termino la transaccion')
