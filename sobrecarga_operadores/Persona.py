class Perosna:

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def __add__(self, other):

        return f'{self.nombre} {other.nombre}'

    def __sub__(self, other):

        return self.edad-other.edad

Persona1=Perosna('juan',30)
Persona2=Perosna('julian',10)
print(Persona1+Persona2)
print(Persona1-Persona2)