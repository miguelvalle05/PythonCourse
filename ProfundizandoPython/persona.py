class Persona:

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

    def __str__(self):
        return f'nombre: {self.nombre} apellido: {self.apellido} id: {hex(id(self)).upper()}'


if __name__ =='main':
    perosna1=Persona('juan','perez')
    print(perosna1)

def mostrar_mensaje(mensaje):
    print(mensaje)