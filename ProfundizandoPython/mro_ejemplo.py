class Clase1:
    def __init__(self):
        print('Clase1.__init__')
    def metodo(self):
        print('Metodo clase1')


class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()
    def metodo(self):
        print('Metodo clase2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()
    def metodo(self):
        print('Metodo clase3')
        super().metodo()

class Clase4(Clase2,Clase3):
    def metodo(self):
        print('Metodo clase 4')
        super().metodo()

#creamos objeto clase 4
clase4=Clase4()
#clases padre de la clase 4 __bases__
print(Clase4.__bases__)
#orden de resolucion de la clase 4
print(Clase4.__mro__)
clase4.metodo()