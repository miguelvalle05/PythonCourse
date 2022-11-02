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
                consulta='DELETE FROM persona WHERE id_persona IN %s'

                entrada=input('Proporciona valor a eliminar separado por comas: ')
                valores=(tuple(entrada.split(',')),)

                cur.execute(consulta,valores)
                registros_eliminados=cur.rowcount
                print(f'registros eliminados: {registros_eliminados}')



except Exception as e:
    print(f'Ocurrio errror: {e}')
finally:
     conexion.close()
