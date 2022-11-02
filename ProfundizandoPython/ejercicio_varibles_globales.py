#definimos varibale local}

contador=0


def mostrar ():
         print(contador)

def modificar_contador(c):

    global contador
    contador=c

modificar_contador(3)

mostrar()

