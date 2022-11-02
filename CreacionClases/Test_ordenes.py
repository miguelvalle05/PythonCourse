from Orden import Orden
from Producto import Producto

producto1 = Producto('amortiguador', 1250)
producto2 = Producto('filtro aceite', 164)
producto3 = Producto('filtro gasolina', 1164)
producto4 = Producto('filtro aire', 1764)
productos= [producto1,producto2]
productos2=[producto3,producto4]

orden1=Orden(productos)
orden1.agregar_producto(producto3)
orden1.agregar_producto((producto4))
print(orden1)
print(orden1.calcular_total())
orden2=Orden(productos2)
print(orden2)
print(orden2.calcular_total())
