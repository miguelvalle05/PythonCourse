#simulacion de sobrecarga de constructores en oython

class Persona:
    def __init__(self,nombre,apellido):
        self.apellido=apellido
        self.nombre=nombre

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)
    @classmethod

    def crear_persona_valores(cls,nombre,apellido):
        return cls(nombre,apellido)



    def __str__(self):
        return f'Nombre {self.nombre}, Apellido {self.apellido}'


persona1=Persona('juan','perez')
persona2=Persona.crear_persona_vacia()
print(persona2)
print(persona1)
#crear persona con clase estatica
persona3=Persona.crear_persona_valores('karla','gomez')
print(persona3)


