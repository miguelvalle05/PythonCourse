import psycopg2

conexion= psycopg2.connect(
    user='postgres',
    password='admin',
    host='localhost',
    port='5432',
    database='test_db'
)


try:
        with conexion:
            with conexion.cursor() as cur:

                   sentencia='INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
                   valores=(('raul','Lara','emaillara'),
                            ('victor','Lara','emaillara'),
                            ('luis','Lara','emaillara'))
                   cur.executemany(sentencia,valores)
                   #conexion.commit ya no va esta linea por que estamos usando with
                   registros_insertados=cur.rowcount
                   print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio errror: {e}')
finally:
     conexion.close()
