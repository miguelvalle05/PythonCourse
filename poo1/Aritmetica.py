class Aritmetica:
    """
             DocString--> Clase aritmetica para sumar,restar, etc
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA=operandoA
        self.operandoB=operandoB


    def sumar(self):
        return self.operandoA+self.operandoB

    def restar(self):
        return  self.operandoA-self.operandoB
    def multiplicar(self):
        return self.operandoA*self.operandoB
    def dividir(self):
        return self.operandoA/self.operandoB



aritmetica1= Aritmetica(5,7)
print(f"{aritmetica1.sumar()}  {aritmetica1.restar()}  {aritmetica1.multiplicar()}  {aritmetica1.dividir()}")


class Rectangulo:
    """
                DocString--> Clase area del rectangulo
       """

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura


rectangulo=Rectangulo(4,5)
print(rectangulo.area())


class Cubo:
    """
                DocString--> Clase volumen de cubo
       """
    def __init__(self,ancho,profundo,alto):
        self.ancho=ancho
        self.profundo=profundo
        self.alto=alto

    def volumen(self):
        return self.ancho*self.profundo*self.alto

cubo1=Cubo(4,5,8)
print(cubo1.volumen())