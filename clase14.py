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
for numero in generador_fibonacci(fin):
    print (numero)

## resumen ##
## Iteradores: Necesitan definir explícitamente los métodos __iter__() y __next__().
## Generadores: Se definen usando una función con yield.

## reto: generadoires de pares e impares:

def generador_pares(limite):
    numero = 0
    while numero < limite:
        numero +=2
        yield numero

def generador_impares(limite):
    numero = 1
    while numero < limite:
        numero += 2
        yield numero 
print("par")

for par in generador_pares(20):
    print(par)


print("impar")
for impar in generador_impares(21):
    print(impar)

def par_impar_generator(limite, modo):
    numero=0
    while numero < limite:
        numero += 1
        if modo == "par":
            if numero % 2 == 0:
                yield numero
        elif modo == "impar":
            if numero % 2 == 1:
                yield numero
        else:
            print("debe escribir par o impar")
            break
print("generador de ambos")
for numero in par_impar_generator(20,"impar"):
    print(numero)