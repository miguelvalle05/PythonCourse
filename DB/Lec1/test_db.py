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

                    consulta='SELECT * FROM persona WHERE id_persona IN %s'
                    #id_persona=input('proporciona id')
                    #llaves_primarias=((1,2),)
                    entrada=input('proporciona las llaves primarias')
                    llaves_primarias=(tuple(entrada.split(',')),)
                    cur.execute(consulta, llaves_primarias)
                    registros=cur.fetchall()
                    for registro in registros:

                        print(registro)
except Exception as e:
    print(f'Ocurrio errror: {e}')
finally:
     conexion.close()
