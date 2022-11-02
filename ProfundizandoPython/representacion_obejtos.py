#representacion de objetos (str,rep,format)


#print(dir(object))

class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    #repr mas enfocado a los programadores
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre:{self.nombre},apellido:{self.apellido})'

    #str para usuario final o otros sistemas

    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # format implementacion por defaulñt es el metodo str
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} con apellido {self.apellido}'


persona1=Persona('juan','perez')
#repr
print(f'Mi objeto persona1: {persona1!r}')
#str de manera automatica el metodo print llama al metodo str
print(persona1)

#formar lleva un f sring
print(f'{persona1}')