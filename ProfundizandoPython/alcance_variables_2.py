#mas de funciones anidades y alcance de variables

def funcion_externa():
    variable_local_externa = 'variable local externa'


    def funcion_anidada():
        variable_local_anidada='variable local anidad'
        nonlocal variable_local_externa
        variable_local_externa='nuevo valor de la variable local externa'

    funcion_anidada()
    print(f'valor de la variable local externa: {variable_local_externa}')






#no es posible acceder a una variable local mas interna
funcion_externa()