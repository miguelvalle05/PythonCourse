import math
from decimal import Decimal

#NaN ----> Not a Number ----> no es sensible a mayusculas/minusculas
#Nan -----> es un tipo de dato numerico indefinido
a=float('NaN')
print(f'a: {a}')
print(f'Es Nan  {math.isnan(a)}')

a=Decimal('nan')
print(f'a: {a}')
print(f'Es Nan  {math.isnan(a)}')