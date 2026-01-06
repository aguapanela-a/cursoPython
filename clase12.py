### poiedra papelotijeras con if, elif y else ###
import random
jugador1 = input("Ingrese su nombre jugador 1")
jugador2 = input("Ingrese su nombre jugador 2")
opciones = {1: "piedra", 2: "papel", 3: "tijera"}


eleccion_j1 = random.randint(1,3)
eleccion_j2= random.randint(1,3)

if eleccion_j1 == 1:
    print(f"{jugador1} eligió piedra")
    if eleccion_j2 == 1:
         print(f"{jugador2} eligió piedra \n Hay empate")

    if eleccion_j2 == 2:
          print(f"{jugador2} eligió papel \n Ganó {jugador2}")
        
    if eleccion_j2 == 3:
         print(f"{jugador2} eligió tijera \n Ganó {jugador1}")
elif eleccion_j1 == 2:
    print(f"{jugador1} eligió papel")
    if eleccion_j2 == 1:
         print(f"{jugador2} eligió piedra \n Ganó {jugador1}")
    if eleccion_j2 == 2:
          print(f"{jugador2} eligió papel \n Hay empate")
        
    if eleccion_j2 == 3:
         print(f"{jugador2} eligió tijera \n Ganó {jugador2}")
else: # eleccion_j1 == 3 
    print(f"{jugador1} eligió tijera")
    if eleccion_j2 == 1:
         print(f"{jugador2} eligió piedra \n Ganó {jugador2}")
    if eleccion_j2 == 2:
          print(f"{jugador2} eligió papel \n Ganó {jugador1}")
        
    if eleccion_j2 == 3:
         print(f"{jugador2} eligió tijera \n Hay empate")


