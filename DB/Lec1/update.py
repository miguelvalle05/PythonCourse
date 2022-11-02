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
                consulta='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
                valores=(('juan','jaurez','email',1),
                         ('juanitooooooooo', 'jaurez', 'email', 2)
                         )


                cur.executemany(consulta,valores)
                registros_actualizados=cur.rowcount
                print(f'registros actualizados: {registros_actualizados}')



except Exception as e:
    print(f'Ocurrio errror: {e}')
finally:
     conexion.close()
