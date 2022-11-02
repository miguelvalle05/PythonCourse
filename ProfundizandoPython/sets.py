#profundizar en set
#set es mutable con elementos unicos
#sus elemntos del son inmutable

conjuntos={'juana',10,True}
print(conjuntos)
#set vacio
conjunto=set()
print(type(conjunto))
conjunto.add('ranses')
print(conjunto)
conjunto.add('ranses')
print(conjunto)
#set a partir de un iterable
conjunto=set([2,3,1,4,2])
print(conjunto)
#podemos agregar mas elementos o incluso un set
conjunto2={100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,4,40,50,50])
print(conjunto)
#copia poco profunda solo se copian referencias
conjunto_copia=conjunto.copy()
print(conjunto_copia)
#verificar igualdad de copias
print(conjunto==conjunto_copia)
print(conjunto is conjunto_copia)

#opreciones con set
pelo_negro={'juan','luis','miguel','maria'}
pelo_rubio={'karen','cristal','marcos','paola'}
ojos_cafe={'miguel','paola'}
menores_30={'juan','miguel','maria'}
#unioon
print(ojos_cafe.union(pelo_rubio))
#invertir union
print(pelo_rubio.union(ojos_cafe))
#intersection
#solo personas de ojos cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))
#difference
#pelo negro sin ojos color cafe
print(pelo_negro.difference(ojos_cafe))
#diferencia simetrico
#pelo negro u ojos color cafe pero no ambas
print(pelo_negro.symmetric_difference(ojos_cafe))
#preguntar si un set esta contenido en otro
#revismaos
print(menores_30.issubset(pelo_negro))
#superset
#si un set contiene a otro subset
print(menores_30.issuperset(pelo_negro))
#distjoint
#dos conjuntos que no tiene algo en comun
print(pelo_negro.isdisjoint(pelo_rubio))