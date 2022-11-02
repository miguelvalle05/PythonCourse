from abc import ABC, abstractmethod

class FiguraGeometrica (ABC):
    def __init__(self, ancho, alto):
        if self._validar_(ancho):
            self._ancho=ancho

        else:
            self._ancho=0
            print('erroneo')
        if self._validar_(alto):
            self._alto=alto
        else:
            self._alto=0
            print('error')
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,ancho):
        if self._validar_(ancho):
            self._ancho=ancho
        else:
            print('error de ancho')


    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self,alto):

        if self._validar_(alto):
            self._alto=alto
        else:
            print('error de alto')

    @abstractmethod
    def calcularArea(self):
        pass



    def __str__(self):
        return f'Figura Geometrica :  Ancho:{self._ancho} Alto:{self._alto}'

    def _validar_(self,valor):
        return True if 0<valor<10 else False