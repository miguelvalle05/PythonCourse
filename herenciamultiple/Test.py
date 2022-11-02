from Cuadrado import *
from Rectangulo import *

print('Creacion Cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(3,'verde')
print(cuadrado1)

print('Creacion Rectangulo'.center(50,'-'))
rectangulo1=Rectangulo(-5,4,'verde')

print(rectangulo1.calcularArea())
