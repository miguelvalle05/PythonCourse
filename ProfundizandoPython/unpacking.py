valores=1,2,3
print(valores)
print(type(valores))
valor1,valor2,valor3=1,2,3
print(valor1,valor2,valor3)
valor1,_,valor2=2,3,4
print(valor1,valor2)
valor1,valor2,*valor3=1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3)
valor1,valor2,*valor3,valor4,valor5=1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3,valor4,valor5)
valor1,valor2,*valor3,valor4,valor5=[1,2,3,4,5,6,7,8,9]
print(valor1,valor2,valor3,valor4,valor5)

def regresa_varios_datos():
    return 7,2,3

valor1,valor,valor3=regresa_varios_datos()

print(valor1,valor2,valor3)

# help(str.partition)

hora,separador,minutos='12:33'.partition(':')
print(hora,minutos)