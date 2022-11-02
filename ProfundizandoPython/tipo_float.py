#profundizaando tipo float
a=3.2

print(f'a: {a:.2f}')
#constructor float puede recibir int y string
a=float(10)
a=float('12')
print(f'a: {a:.2f}')
#Notacion exponencial (valores positivos y negativos)
a=3e5
#Cualquier calculo que involucre un float, se promueve a float
a=4.0+5
print(f'a: {a}')