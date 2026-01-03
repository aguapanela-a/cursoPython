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
print(nombre.join(["Un saludo señor ", ", te amo"])) # Une elementos con el string nombre como separador (lo pone entre cada elemento)
print(nombre.replace("e", "a")) # Reemplaza 'e' por 'a


#Capitaliza la primera letra.

texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"

#title()
#Capitaliza la primera letra de cada palabra.
texto = "hola mundo"
print(texto.title())  # "Hola Mundo"

#strip()
#Elimina los espacios en blanco al inicio y al final.
texto = "  hola  "
print(texto.strip())  # "hola"

#replace(old, new)
#Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # "hola Python"

#split(sep)
#Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']

#join(iterable)
#Une elementos de un iterable en una sola cadena.
lista = ["hola", "mundo"]
print(" si ".join(lista))  # "hola mundo"

#find(sub)
#Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))  # 5

#startswith(prefix) y endswith(suffix)
#Verifica si la cadena empieza o termina con una subcadena.
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.endswith("mundo"))  # True

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"