
class Producto():
   contador_productos =0


   def __init__(self,nombre,precio):
       Producto.contador_productos +=1
       self._id_productos=Producto.contador_productos
       self._nombre=nombre
       self._precio=precio


   @property
   def precio(self):
       return self._precio




   def __str__(self):
        return f'id: {self._id_productos} Nombre: {self._nombre} Preci0: {self._precio}'



if __name__=='__main__':

    producto1=Producto('amortiguador',1250)
    print(producto1)
    producto2=Producto('filtro aceite',164)
    print(producto2)



