from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('hp', 'usb')
raton1 = Raton('hp', 'usb')
monitor1 = Monitor('hp', 24)
computadora = Computadora('hp', monitor1, teclado1, raton1)

teclado2 = Teclado('ibm', 'usb')
raton2 = Raton('ibm', 'usb')
monitor2 = Monitor('ibm', 24)
computadora2 = Computadora('ibm', monitor2, teclado2, raton2)

teclado3 = Teclado('gamer', 'usb')
raton3 = Raton('gamer', 'usb')
monitor3 = Monitor('gamer', 24)
computadora3 = Computadora('gamer', monitor2, teclado2, raton2)


comptadoras1 =[computadora,computadora2]
orden=Orden(comptadoras1)
print(orden)
orden.agregar_computadora(computadora3)
print(orden)

computadoras2=[computadora3,computadora2]
orden2=Orden(computadoras2)
print(orden2)

