# class persona:
#     def __init__(self, nombre, apellido,edad,*tupla,**diccionario):
#         self._nombre=nombre
#         self.apellido=apellido
#         self.edad=edad
#         self.tupla=tupla
#         self.diccionario=diccionario
#
#     def motrarDetalle(self):
#         print(f'Persona {self._nombre} {self.apellido} {self.edad} {self.tupla}{self.diccionario}')
#         pass
#
# Persona1 = persona('juan','perez',55, 23432432432,444,3,d='hola',r='wewr')
# Persona1.motrarDetalle()

class Persona:
    def __init__(self, nombre, apellido,edad):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad

    @property
    def nombre(self):
        print("metodo get")
        return  self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("metodo set")
        self._nombre=nombre

    @property
    def apellido(self):
        print("metodo get")
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        print("metodo set")
        self._apellido = apellido

    @property
    def edad(self):
        print("metodo get")
        return self._edad

    @edad.setter
    def edad(self, edad):
        print("metodo set")
        self._edad = edad

    def motrarDetalle(self):
        print(f'Persona {self._nombre} {self._apellido} {self._edad} ')
        pass

    def __del__(self):
        print(f'Persona: {self._nombre}{self._apellido}{self._edad}')
if __name__ == '__main__':

   Persona1 = Persona('juan','perez',55)
   Persona1.nombre='sdfsdfsdf'
   Persona1.apellido='qqweqwe'
   Persona1.edad=3
   Persona1.motrarDetalle()