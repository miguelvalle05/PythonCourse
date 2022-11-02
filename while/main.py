contador =5

while contador>=1:
    print(contador)
    contador -=1
else:
    print("fin del ciclo while")

#ciclo for


for letra in 'Holaana':
    if letra=='a':
        print(f'Se encontra la letra {letra}')
        break
else:
    print("fin ciclo for")



for i in range(6):

    if i%2==0:
        print(i)

for i in range(6):

    if i%2 !=0:
        continue
    print(i)
