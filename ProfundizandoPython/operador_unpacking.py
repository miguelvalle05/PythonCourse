#desempaquetar



numeros=[1,2,3]
print(numeros)
print(*numeros,sep=" - ")

#desempaquetar diccionarios con **


def sumar(a,b,c):
    print(f'Resultado de la suma: {a+b+c}')


sumar(*numeros)


# extraer algunas partes de una lista
mi_lista=[1,2,3,4,5,6]
a,*b,c,d=mi_lista
print(a,b,c,d)


#UNIR LISTAS
lista1=[1,2,3]
lista2=[4,5,6]
lista3=[lista1,lista2]
print(lista3)
lista3=[*lista1,*lista2]
print(lista3)


#unir diccionarios
dic={'A':3,'B':4,'C':6}
dic2={'D':8,'E':1}
dic3={**dic, **dic2}
print(dic3)


#construit lista  a aprtir de un string

lista=[*'hoolamundo']
print(lista)
print(*lista)

