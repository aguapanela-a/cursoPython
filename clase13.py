## Iteración y control de flujo con bucles en Python ##
lista = [1,2,3,4,5,6,7,9]
for i in lista:
    print(f"El valor de i en lalista es: {i}")

for  i in range(10):
    print(f"Elvalor de i en el ango del 0 al 9 es: {i}")
    for j in range(4,15, 3):
        print(f"El valor de j en el rando de 4 a 15 es de {j}")
    if i == 7:
        print("7 encontrado por i")

contador = 0
while  contador <= 100:
    contador+=1
    if contador == 18:
        continue
    print(f"El valor delcontador en while es de {contador}")
    if contador == 20:
        print(f"contador llegó a  {contador}, entonces se acaba el ciclo")
        break