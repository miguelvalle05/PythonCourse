from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:

    contador_computadoras=0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras+=1
        self._id_computadora=Computadora.contador_computadoras
        self._nombre=nombre
        self._monitor=monitor
        self._teclado=teclado
        self._raton=raton

    def __str__(self):
        return f'''
          {self._nombre}: {self._id_computadora}
          Monitor: {self._monitor}
          Teclado: {self._teclado}
          Raton:   {self._raton}
          '''
if __name__=='__main__':
    teclado1=Teclado('hp','usb')
    raton1=Raton('hp','usb')
    monitor1=Monitor('hp',24)
    computadora=Computadora('hp',monitor1,teclado1,raton1)
    print(computadora)
    teclado2 = Teclado('ibm', 'usb')
    raton2 = Raton('ibm', 'usb')
    monitor2 = Monitor('ibm', 24)
    computadora2 = Computadora('ibm', monitor2, teclado2, raton2)
    print(computadora2)