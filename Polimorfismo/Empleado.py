class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo

    def __str__(self):

        return f'EMPELADO: [NOMBRE: {self.nombre} SUELDO:{self.sueldo}]'

    def mostrat_detalle(self):
        return self.__str__()


