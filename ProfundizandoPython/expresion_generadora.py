#expresion generador
#es ungenerador anonimo

multiplicacion=(valor*valor for valor in range(4) )

print(multiplicacion)
print(type(multiplicacion))

print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))



# se puede pasar una expresion generadora a una funcion sin parentesis
import math

suma=sum(valor*valor for valor in range(4))
print(suma)


#tambien podemos usar una lista o cualquier otro iterador
lista=['juan','perez']
generador= (valor for valor in lista)
print(next(generador))


#crear string a partir de un generador creado a partir de una lista


lista=['karla','gomez']
contador=0
#defenimos una funcion para incrementar el contador
def incrementar():
    global contador
    contador+=1
    return contador

# la primera parte es el yield del generador
#segunda parte es el for en parentesis

generador=(f'{incrementar()}.{nombre}' for nombre in lista)
lista=list(generador)
print(lista)


cadena=', '.join(lista)
print(cadena)
