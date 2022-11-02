# #Profundizando en tipo STR
# from mi_clase import MiClase
# #concatenacion automatica de python
#
#
# #help(MiClase)
#
# print(MiClase.__doc__)
# print(MiClase.__init__.__doc__)
# print(MiClase.mi_metod.__doc__)
#
# mensaje='Hola'+'Mundo'
# mensaje+='pythion'
# print(mensaje)
# help(str.capitalize)

#
# help(str.capitalize)
# mensaje1='hola mundo'
# mensaje2=mensaje1.capitalize()
#
# print(f'mensaje1: {mensaje1} id1:{id(mensaje1)} mensaje 2: {mensaje2} id2:{id(mensaje2)}')
#
# mensaje1+='saludos'
# print(f'mensaje1: {mensaje1} id1:{id(mensaje1)} mensaje 2: {mensaje2} id2:{id(mensaje2)}')

#help(str.join)
# tupla_str=('hola', 'mundo','universidad')
# mensaje=' '.join(tupla_str)
# print(mensaje)
# lista_cursos=['java','python','angular','spring']
# mensaje2=','.join(lista_cursos)
# print(mensaje2)
# cadena='holamundo'
# mensaje3='.'.join(cadena)
# print(mensaje3)
# diccionario={'nombre':'juan','apellido':'perez'}
# mensaje4='-'.join(diccionario.keys())
# mensaje5='-'.join(diccionario.values())
# print(mensaje4)
# print(mensaje5)

# #help(str.split)
#
# cursos='java javascript python angulat c++'
# listacursos=cursos.split()
# print(listacursos)
#
# cursos_coma='c#,angular,java,spring'
# lista_cursos=cursos_coma.split(',')
# print(lista_cursos)
#
# cursos_coma='c#,angular,java,spring'
# lista_cursos=cursos_coma.split(',',2)
# print(lista_cursos)

#dar formato a un string
# nombre="juan"
# edad=19
# sueldo=123
# mensaje='Nombre {} edad {} sueldo {:.2f}'.format(nombre,edad,sueldo)
# print(mensaje)
# mensaje_conformato='Nombre {0} edad {1} sueldo {2:.2f}'.format(nombre,edad,sueldo)
# print(mensaje_conformato)
# mensaje_conformato='Nombre {n} edad {e} sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
# print(mensaje_conformato)

# persona=('karla','gomez',5000)
# # mensaje_conformato='hola %s %s tu sueldo es %.2f'%persona
# # print(mensaje_conformato)
# mensaje_conformato='hola %s %s tu sueldo es %.2f'
# print(mensaje_conformato%persona)

# nombre="juan"
# edad=19
# sueldo=123
#
#
# # diccionario={'nombre':'ivan','edad':35,'sueldo':1500}
# # mensaje_conformato='Nombre {persona[nombre]} edad {persona[edad]} sueldo {persona[sueldo]}'.format(persona=diccionario)
# # print(mensaje_conformato)
#
# nombre="juan"
# edad=19
# sueldo=123
# mensaje_conformato=f'Nombre {nombre} edad {edad} sueldo {sueldo:.2f}'
# print(mensaje_conformato)
#
# print(nombre,edad,sueldo, sep=',')


# #multiplicacion de cadenas
# resultado=5*'hola'
# print(resultado)
# #multiplicacion de tuplas
# resultado=3*('Hola','Mundo')
# print(resultado)
# #multiplicacion de listas
# resultado=4*[0]
# print(resultado)

# #carcteres de escape
# resultado='hola \' mundo '
# print(resultado)
# #backspace
# resultado='hola\b\b mundo '
# print(resultado)
# #caracter\
# resultado='c:\\directorio\\archivo '
# print(resultado)
# #raw str
# resultado=r'c:\\directorio\\archivo '
# print(resultado)


# #caracteres unicode
# print('Hola\u0020Mundo')
# print('Hola\u0041Mundo')
# print('Hola\U00000044Mundo')
# print('Hola\x41Mundo')
# print('Hola\u263AMundo')
# #caracteres ASCII
# caracter=chr(65)
# print(caracter)
# caracter=chr(64)
# print(caracter)

#carcateres de tipo byte
#
# caracteres_en_bytes=b'Hola mundo'
# print(caracteres_en_bytes)
# mensaje=b'Hola universidad python'
# print(mensaje[1])
# print(chr(mensaje[1]))
#
# lista_caracteres=mensaje.split()
# print(lista_caracteres)


# convertir de str a bystes
string='Progración con python'
print('String original: ',string)
bytes=string.encode('utf-8')
print('byets codificado ',bytes)
string2= bytes.decode('utf-8')
print("string decodificado: ", string2)
print(string==string2)
