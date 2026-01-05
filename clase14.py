### iteradoresy generadores enpyhon ###

#iteradores, van iterando cada uno de los elementos in utilizar indices
my_list=[1,2,3,4]
my_iter = iter(my_list)

#usar el iterador   (next lo que hace es que nososrtros podamos ir viendo cualessonlosvaores que se van guardandoo almacenando en memoria)
print(next(my_iter), "asdasdad") 
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#dado quelascadenas de texo funcionana conlistas de caracteres 
cadena1 = "Buenos dias mi gentesas"
inter_cad1 = iter(cadena1)

print(next(inter_cad1), "afffafa")
print(next(inter_cad1))
print(next(inter_cad1))
print(next(inter_cad1))

##también se puede isareliter con for
for char in inter_cad1:
    print(char, "iteracion con el for") 

##por la salidad  del terminal se puede observar que las primeras
# 4 carácteres se imprimen con los print manuales
# y el restocon el ciclo for


##iterador de nmerosimpares
limite = 15
iterador_impar = iter(range(1,limite + 1,2))

for impar in iterador_impar:
    print(impar)


####  Generador ###
# fnción queproduce una secuencia de datos en los cuale spodemos iterar
# sin usar return, es como una función con varios return,son yield

def generador_de_saludos(nombres):
    for nombre in nombres:
        yield f"¡Hola, {nombre}!" # Aquí devolvemos un string, no un número

# Uso del generador
usuarios = ["Ana", "Betico", "Carla"]
for saludo in generador_de_saludos(usuarios):
    print(saludo)

#Solo "crean" el elemento que necesitas en el momento exacto en que lo pides (evaluación perezosa o lazy evaluation). Una vez que pasas al siguiente, el anterior puede ser descartado.

#secuencia de fibonacci
# 0 1 1 2 3 5 8 13 21 34 ...

def generador_fibonacci(fin):
    anterior = 0
    fibonacci = 1
    while fibonacci <= fin:
        fibonacci += anterior
        anterior = fibonacci-anterior
        yield fibonacci

fin = 400
for numero in generador_fibonacci(400):
    print (numero)


