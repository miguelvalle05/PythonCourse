#atributos publicos, protegidos y privador

class MiClase:
    def __init__(self,publico,protegido,privado):
        self.publico=publico
        self._protegido=protegido
        self.__privado=privado



objeto=MiClase('valor publico','valor protegido','valor privado')
#acceso al atributo publico
print(objeto.publico)
objeto.publico='nuevo valor publico'
print(objeto.publico)
#Acceso al valor protegido
#solo dentro de la misma clase o clases hijas
print(objeto._protegido)
objeto._protegido='nuevo valor protegido'
print(objeto._protegido)
#Acceso al valor privado
#print(objeto.__privado)
print(objeto._MiClase__privado)
objeto._MiClase__privado='Nuevo valoir privado'
print(objeto._MiClase__privado)