valor1=int(input("Ingresa un primer vaalor "))
valor2=int(input("Ingresa el segundo valor "))


if valor1>valor2:
    print("El mayor es ",valor1)
else:
    print("El mayor es ",valor2)

#programa libros
titulo=input("Titulo del libro ")
id=int(input("Ingresa el ID "))
precio=float(input("Ingresa el precio "))

valorb=bool;

envio=input("El envio es: ")
if envio == 'True':
    valorb=True;
else:
    valorb=False;

print(f"El titulo es: ",titulo)
print(f"El id es ",id)
print("El precio es ",precio)
print("El envio es ",valorb)