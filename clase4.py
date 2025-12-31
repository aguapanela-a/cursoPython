oracion1 = '''Esto es una oración multilinea.
podemos escribir variias lineas en una sola variable.
Incluso con saltos de linea.
Como este.'''
print(oracion1)
print("\n")

oracion2 = """Otra forma de crear oraciones multilinea.
Esto también es una oración multilinea.
Podemos escribir varias lineas en una sola variable.
Incluso con saltos de linea.
Como este."""
print(oracion2)
print("\n")


print("imprimire el caracter en la posioción 5 de la oracion 1")
print("\n" + oracion1[5]) # Imprime el caracter en la posición 5 de oracion1

print("imprimire el caracter en la posioción 15 de la oracion 2")
print(oracion2[15]) # Imprime el caracter en la posición 15 de oracion2

print("imprimire los caracteres desde la posioción 0 hasta la 3 de la oracion 1")
print(oracion1[0:4]) # Imprime los caracteres desde la posición 0 hasta la 3 de oracion1

print("imprime el penúltimo caracter de la oracion 1")
print(oracion1[-2]) # Imprime el penúltimo caracter de oracion1

print("\n")

##operación entre variables tipo string
saludo = "Hola"
nombre = "erick"
print(saludo + " " + nombre) # Concatenación de strings
print("\n")

print(nombre + "_ " + (saludo+" ") * 3) # Concatenación y repetición de strings
print("\n")

##cosultar cantidad de carateres de las cadenas
print("Cantidad de caracteres en las oraciones:")
print(len(oracion1)) # Imprime la cantidad de caracteres en oracion1
print(len(oracion2)) # Imprime la cantidad de caracteres en oracion2}

##metodos para variables
print("\n")
print("Uso de métodos para variables tipo string:")
print(nombre.upper()) # Convierte a mayúsculas
print(nombre.lower()) # Convierte a minúsculas
print(nombre.join(["Mi ", " es genial"])) # Une elementos con el string nombre como separador (lo pone entre cada elemento)
print(nombre.replace("e", "a")) # Reemplaza 'e' por 'a