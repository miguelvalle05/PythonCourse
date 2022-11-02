#una funcion dentro de otra

def calculadora(a,b,operacion='sumar'):

    if(operacion=='sumar'):
        #primero definir funcion
        def suma(a,b):
            return a+b
        #segundo llamar a la funcion
        print(f'Suma: {suma(a,b)}')

    if(operacion=='restar'):

        # primero definir funcion
        def resta(a, b):
            return a - b

        # segundo llamar a la funcion
        print(f'Resta: {resta(a, b)}')



calculadora(3,6,'restar')