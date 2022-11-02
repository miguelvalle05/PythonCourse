from Conexion import Conexion
from Persona import Persona
from cursor_del_pool import CursorDelPool
from logger_base import log


class PersonaDao:

        '''
        DAO (Data Access Object)
        CRUD(Create Read Update Delete)

        '''
        _SELECCCIONAR='SELECT * FROM persona ORDER BY id_persona'
        _INSERTAR='INSERT INTO persona (nombre,apellido,email) VALUES(%s,%s,%s)'
        _ACTUALIZAR='UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
        _ElIMINAR='DELETE FROM persona WHERE id_persona=%s'

        @classmethod
        def seleccionar(cls):

            with CursorDelPool() as cursor:
                cursor.execute(cls._SELECCCIONAR)
                registros= cursor.fetchall()
                personas=[]
                for registro in registros:
                    persona = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona)

                return personas

        @classmethod
        def insertar(cls, persona):
               with CursorDelPool() as cursor:
                    log.debug(f'Persona a insertar: {persona}')
                    valores =(persona.nombre,persona.apellido,persona.email)
                    cursor.execute(cls._INSERTAR,valores)
                    log.debug(f'Persona insertada: {persona}')
                    return cursor.rowcount

        @classmethod
        def actualizar(cls,persona):
               with CursorDelPool() as cursor:
                    valores=(persona.nombre,persona.apellido,persona.email,persona.id_persona)
                    cursor.execute(cls._ACTUALIZAR,valores)
                    log.debug(f'Persona Actualizada:{persona}')
                    return cursor.rowcount

        @classmethod
        def eliminar(cls,persona):
             with CursorDelPool() as cursor:
                    valores=(persona.id_persona,)
                    cursor.execute(cls._ElIMINAR,valores)
                    log.debug(f'Objeto eliminado: {persona}')
                    return cursor.rowcount





if __name__=='__main__':

    #insertar registro
    persona=Persona(nombre='Miguel',apellido='Fernandez',email='pedro@gmail.com')
    personas_insertadas=PersonaDao.insertar(persona)
    log.debug(f'Personas insertadas {personas_insertadas}')

    # #actualizar persona
    # # persona2=Persona(7,'Juan Carlos','Juarez','cjuares@gmail.com')
    # # personas_actualizadas=PersonaDao.actualizar(persona2)
    # # log.debug(f'Personas actualizadas:{personas_actualizadas}')
    #
    # #eliminar una persona
    # persona4=Persona(id_persona=14)
    # personas_eliminadas=PersonaDao.eliminar(persona4)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')
    #



    #selecionar personas
    personas1=PersonaDao.seleccionar()
    for persona in personas1:
        log.debug(persona)

