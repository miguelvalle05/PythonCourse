a = int(input("Escribe un valor numerico"))
if a % 2 == 0:
    print(f"El numero {a} es un numero par")
else:
    print(f"El numero {a} es un unero impar")

# Mayor de edad
adulto = 18
edad = int(input("Escribe tu edad"))
if edad >= adulto:
    print(f"Eres mayor de edad")
else:
    print(f"Eres menor de edad")


# valor en un rango


valor = int(input("Escribe tu valor"))
valorminimo=0
valormaximo=5
rango= (valor>=valorminimo) and (valor<=valormaximo)
if rango:
    print(f"Esta en el rango")
else:
    print(f"No esta en el rango")


#ejemplo operador or
vacaciones=True
descanso=False

if not (vacaciones or descanso):
    print("Tiene deberes por hacer")


else:

    print("Puede asistir al juego")

#rango de edad
edad= int(input("Introduce tu edad"))
veintes = edad>=20 and edad<30
print(veintes)
treintas= edad>=30 and edad<40
print(treintas)

if veintes or treintas:
    print('Dentro de rango (20\'s)o(30\'s')
    if veintes:
        print("dentro de veinte")
    elif treintas:
        print("dentro de treinte")
    else:
        print("fuera de rango")
else:
    print("No esta dentro de los 20´s ni 30´s")
