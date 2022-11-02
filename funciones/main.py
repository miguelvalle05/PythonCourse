def funsumar(*numeros):
    suma=0
    for numero in numeros:

        suma+=numero




    return suma

print(funsumar(4,5,3))


def multi(*numeros):
    mul=1
    for numero in numeros:

        mul*=numero




    return mul

print(multi(4,5,3))


def listarter(**terminos):
    for llave, valor in terminos.items():

        print(f"{llave}:{valor}")


listarter(IDE='IDENTIFICADOR',PK='PRIM')


def desplegarnombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres=['hjuan','ismael','leonardo']
desplegarnombres(nombres)

#recursividad

def factorial(numero):
    if numero==1:
        return 1
    else:
        return numero*factorial(numero-1)

print(factorial(3))



def recu(numero):

    if numero <=0:
        return "error"

    if numero==1:
        return 1
    else:

        print(numero)
        return recu(numero-1)
numero=int
numero=-5
print(recu(numero))


def calculartotal(pago,impuesto):

   total= pago*(1+(impuesto/100))
   return total

print(calculartotal(1000,16))


def celsius_farenheit(celsius):
    return (celsius*9/5)+32

def farenheit_celsius(farenheit):
    return (farenheit-32)*(5/9)

celsius=float(input("ingresa el valor"))

farenheit=float(input("Ingresa el valor"))

print(f"El resultado es {celsius_farenheit(celsius)}")
print(f"El resultado es {farenheit_celsius(farenheit)}")