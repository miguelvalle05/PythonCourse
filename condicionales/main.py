# condicion = True
#
# if condicion == True:
#     print("Condicion Verdadera")
# elif condicion ==False:
#     print("Condicion false")
# else:
#     print("Condicion no reconocida")
#
# numero=int(input("Escribe un numero del 1 al 3"))
# numerotexto= '';
#
# if numero == 1:
#     numerotexto="Es numero uno"
# elif numero==2:
#     numerotexto="Es un numero dos"
# elif numero ==3:
#     numerotexto="Es un numero tres"
# else:
#     numerotexto="fuera de rango"
#
# print(f"el valor es {numero}:{numerotexto}")
#
# condicion1 = False
# print("condicion verdadera")if condicion1 else print("condicion falsa")
#
# mes=int(input("Ingresa un mes de 1-12 "))
# estacion= None
#
# if mes==1 or mes==2 or mes==12:
#     estacion="Invierno"
#
# elif mes==3 or mes==4 or mes==5:
#     estacion="Primavera"
#
#
# elif mes==6 or mes==7 or mes==8:
#     estacion="Verano"
#
#
# elif mes==9 or mes==10 or mes==11:
#     estacion="Otoño"
#
# else:
#     estacion="Mes incorrecto"
#
# print(f"Para el mes {mes} la estacion es {estacion}")

# edad=int(input("Ingresa una edad"))
# etapa= None
#
# if edad>=0 and edad<10:
#     etapa="Infancia Increible"
#
# elif edad>=10 and edad<20:
#     etapa="muchos cambios y muchos estudios"
#
#
# elif edad>=20 and edad<=30:
#     etapa="amor y comienza el trabajo"
#
# else:
#     etapa="Estapa incorrecta"
#
# print(f"Para la edad {edad} la etapa es {etapa}")


numero=int(input("Ingresa un numero entre 1-10"))
calificacion= None

if numero==9 or numero==10:
  calificacion="A"

elif numero==8 :
  calificacion="B"

elif numero==7 :
  calificacion="C"

elif numero==6 :
  calificacion="D"

elif numero<6 :
  calificacion="F"

else:
    calificacion="Incorrecto"


print(f"Para calificacion {numero} corresponde {calificacion}")