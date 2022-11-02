class Persona:
    contador_personas=0
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


persona1= Persona('juan','perez')
print(persona1.__dict__)

#accedemos al atributo de clase
print(persona1.contador_personas)
#pero noes posible modificarlo con el objeto, sino con la clase
# crear atributo al vuelo es decir al momento
persona1.contador_personas=10
print(persona1.__dict__)
print(Persona.contador_personas)#atrbuto de clase
print(persona1.contador_personas)#atributo de objeto

persona2=Persona('luis','gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

#asociar atributo de clase al vuelo

Persona.contador2=20
print(Persona.contador2)