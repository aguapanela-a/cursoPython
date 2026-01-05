##manejo de matrices y tuplas en python 

matrix = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(matrix[0]) #primera fila 
print(matrix[1][1]) #segunda fila y segunda columna
print(matrix[2][0]) #tercera fila y primera columna

#matriz de 3 dimensiones
matrix_3d = [[[1,2,3],[4,5,6],[7,8,9]],
             [[10,11,12],[13,14,15],[16,17,18]],
             [[19,20,21],[22,23,24],[25,26,27]]]


print(matrix_3d[1][1][1]) #segunda fila, segunda columna, segunda profundidad

## tuplas: es una colección de datos inmutable, es decir, no se puede modificar su contenido una vez creada. Se definen con paréntesis ()
tupla = (1,2,3,4,5)
print(tupla)
print(type(tupla))
#tupla[0] = 10 #esto generará un error porque las tuplas son inmutables

#sin empbargo se Pueden modificar listas dentro de una tupla,pues estas son mutables
variable1 = 345
tupla2 = (variable1, "hola", [1,2,3])
print(tupla2)
tupla2[2][1] = 999
print(tupla2)

#desempaquetado de tuplas
tupla3 = (10,20,30)
a,b,c = tupla3
print(a)
print(b)
print(c)