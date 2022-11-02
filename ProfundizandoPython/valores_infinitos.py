# Manejo de valores inifinitos
import math
from decimal import Decimal
infinito_positivo=float('inf')
print(f'infinito poaitivo: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)} ')
infinito_negativo=float('-inf')
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)} ')
#modulo math
inifinito_positivo= math.inf
print(f'infinito poaitivo: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)} ')

infinito_negativo= -math.inf
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)} ')
#modulo decimal

inifinito_positivo= Decimal('infinity')
print(f'infinito poaitivo: {infinito_positivo}')
print(f'Es infinito: {math.isinf(infinito_positivo)} ')

infinito_negativo= Decimal('-infinity')
print(f'infinito negativo: {infinito_negativo}')
print(f'Es infinito: {math.isinf(infinito_negativo)} ')