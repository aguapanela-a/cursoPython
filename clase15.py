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