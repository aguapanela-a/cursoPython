##si creo una lista a y luego hago a = b ambos auntarán al msmo espacio en memoria, es decir, lo que pase a "a" pasará también en "b"
a = [1,2,3,4,5,6]
b=a
print(a)
print(b)

#espacios en memoria:
print(id(a))
print(id(b))

##para evitar esto se puede usar slicing  así:
c = a[:]

print("espacio en memoria de a ",id(a))
print("espacio en memoria de b ",id(b))
print("espacio en memoria de c ",id(c))

##t ambién podemos usar el método .copy()
d = a.copy()

print("espacio en memoria de d ",id(d))

## si agrego algo a "a" de verá reflejado en "b" pero en el resto no
a.append(345)

print(a,b,c,d)
