#Alcance de variables(scope)

var_global='varibale global'

def imprimir():
    #acceder a una variable gloabl

    #modificar la varible global

    global var_global

    print(f'desde funcion: {var_global}')
    #definir varible loca
    var_local='Variable local'
    print(f'desde funcion variable local {var_local}')
    var_global='nuevo valor de la varible global'

    def funcion_anidad():
        print(f'variable local en fucnion anidada: {var_local}')

    funcion_anidad()


imprimir()
print(f'variable global fuera de funcion {var_global}')
