#generadores
#ers una funcion especial en python que regresa una secuencia de valores
#susoende la ejecucion de la funcion yield(producir) no se usa return
def generador():
    yield 1
    print("se reanuda")
    yield 2
    print("se reanuda")
    yield 3
    print("se reanuda")


# consumimos generador a demanda

gen = generador()
#con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen))
#si tratamos de consumir mas de unvalor de los que produce nos manda error


#consumiendo valores de generador con for
gen=generador()

for valor in gen:
    print(f"numero generado {valor}")