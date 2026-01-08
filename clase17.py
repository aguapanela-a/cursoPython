## Funciones lambda en python ##
# son funciones de operaciones rápidas que no necesitan definirse un nombre, solo parámetros necesarios y lo que retornará, así
suma = lambda a, b : a + b
print(suma(1,5))

## funciones lamba con map para cuando quiero aplicar una función a cada elemento de una lista, así:
numeros = list(range(11)) ## numeros será una lista con osnúmeros del 0 al 10
cuadrados = list(map(lambda x: x**2, numeros))  ## la función lambda será aplicada a cada elemento de números (map) de la nueva lista cuadrados (list)
print(f"Números: {numeros} \nCuadrados: {cuadrados}")

#map(se aplcará esto, a esto)

## ahora usarémos función filter() para filtrar elementos que complen con una condición
