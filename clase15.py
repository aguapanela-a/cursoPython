import random
## listasporcomprensión ##
# eslaforma en laque pueden crear listas defrma breve, evitando largos bucles
# permiten creas listas de forma consiza expresiva y eficiente
# ara crear,istas usando una linea de codigo
# utilizar otras listas queserá modificadas paracrear una nueva
# y tilización del if y del for 
#list_comprension: [expresion for item iterable if condición]

# creación de cuadrados
# 1 4 9 16 25 36 ...

squares = [x**2 for x in range(1,20)] #quiero se eleve alcuadrado para cada x en elrango de 1 al 19
print(squares)

celcius = []
for x in range(1,20):
    y = random.randint(1,100)
    celcius.append(y)
    
fahrenheit =[((9/5)*x+32) for x in celcius]

print(f"Grados celsius: {celcius} \n Grados fahrenheit: {fahrenheit}" )

pares =[x for x in range(0,16,2)]
print("pares ", pares)

imapres =[x for x in range(1,31) if x%2==1]
print(f"impares: {imapres}")

## matriz transpuesta ##
matriz= [[1,2,3],
         [4,5,6],
         [7,8,9]]

transpose = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
# 1,4,7
# 2,5,8
# 3,6,9

# para i = 0, va a meter en la fila 0 la posición 0 de cada una de las filas de la matriz
# para i = 1, va a meter en la fila 1 la posición 1 de cada una de las filas de la matriz
# para i = 2, va a meter en la fila 2 la posición 2 de cada una de las filas de la matriz