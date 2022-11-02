from numeros_identicos_exception import NumerosIdenticosException

resultado=None


try:
    a = int(input('Primer numero'))
    b = int(input('segundo numero'))

    if a==b:
        raise NumerosIdenticosException('numeros identicos')
    resultado=a/b
except Exception as e:
   print(f'Ocurrio error: {e} {type(e)}')


except TypeError as e:
   print(f'Ocurrio error: {e} {type(e)}')

except ValueError as e:
   print(f'Ocurrio error: {e} {type(e)}')

except Exception as e:
   print(f'Ocurrio error: {e} {type(e)}')

else:
    print('No se arrojo ninguna exepcion')

finally:

    print('bloque finally')



print(f'El resultado es: {resultado}')
print(f'Continumamos.....')