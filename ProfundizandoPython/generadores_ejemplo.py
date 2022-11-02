#Generador de numeros del uno al 5


def generador_numeros():

    for numero in range(1,6):
        yield numero
        print("se reanuda la ejecucion")




#objeto generador

generador=generador_numeros()

print(f'objeto generador {generador}')
print(f'tipó: {type(generador)}')

#consumimos valores del generador

for valor in generador:
    print(f'numero producido: {valor}')
# consumir a demqanda
generador=generador_numeros()

#cachar errror cuando coinsumimos todo el generador

try:

        print(f'consumimos a demanda el generador {next(generador)}')
        print(f'consumimos a demanda el generador {next(generador)}')
        print(f'consumimos a demanda el generador {next(generador)}')
        print(f'consumimos a demanda el generador {next(generador)}')
        print(f'consumimos a demanda el generador {next(generador)}')
        print(f'consumimos a demanda el generador {next(generador)}')

except StopIteration as e:
    print("Error al consumir generador")



#otra forma de consumir generador

generador=generador_numeros()

while True:
    try:
        valor= next(generador)
        print(f'Impresion de valor generado: {valor}')
    except StopIteration as e:
        print('se termino de iterr el generador')
        break

