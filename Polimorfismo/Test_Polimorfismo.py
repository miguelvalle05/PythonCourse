from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrat_detalle())
    if isinstance(objeto,Gerente):
     print(objeto.departamento)


empleado=Empleado('juanito',123)
imprimir_detalles(empleado)

gerente=Gerente('juanito',2345,'sistemas')
imprimir_detalles(gerente)