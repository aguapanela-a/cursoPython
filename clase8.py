lista_mixta =[19, "string", ["a",3,3.23], 3.34e-3, False, True]
print(lista_mixta)
print("Ultimo elemento: ", lista_mixta[-1])
print("Tercer elemento: ", lista_mixta[2])
print("Del segundo al quinto elemento", lista_mixta[1:5])
print("Del  tercer elemento al ukltimo: ", lista_mixta[2:])
print("Del inicio al cuarto elemento: ", lista_mixta[:4])

# Modificación de listas
##modificar algun elemento por su indice
print("lista original: ", lista_mixta)
print("Modifico el segundo elemento")

lista_mixta[1] = "nuevo valor"
print("lista modificada: ", lista_mixta)

##convierto primerelemento a string
print("Modifico el primer elemento")
lista_mixta[0] = str(lista_mixta[0])
print("lista modificada: ", lista_mixta)

##agrego elementos alfinalcon append
lista_mixta.append(67776)
print("lista con nuevos elementos al final: ", lista_mixta)

##agrego elementos en una posicion especifica con insert
lista_mixta.insert(3, "valor nuevo en posicion 3")
print("lista con nuevo elemento en posicion 3: ", lista_mixta)

##elimino elementos por su indice con del (ojo: elimina el elemento de memoria, si hago "del lista_mixta" borro toda la lista,y sale como si no estuviera definida)
print("Elimino el cuarto elemento")
del lista_mixta[3]
print("lista con el cuarto elemento eliminado: ", lista_mixta)  

##elimino un elemento por su valor con remove
lista_mixta.remove('19')
print("lista con el elemento '19' eliminado: ", lista_mixta)

##elimino el ultimo elemento con pop
lista_mixta.pop()
print("lista con el ultimo elemento eliminado con .pop: ", lista_mixta)

##elimino un elemento en una posicion especifica con pop
lista_mixta.pop(1)
print("lista con el segundo elemento eliminado con pop", lista_mixta)

##buscar la posición de un elemento con index
print("la posición del elemento 0.00334 es: ", lista_mixta.index(0.00334)) ##si hay un valor repetido, devuelve la posicion de la primera ocurrencia

##contar cuantas veces aparece un elemento con count
lista_mixta.append(True)
print("lista con un nuevo True agregado: ", lista_mixta)
print("El valor True aparece ", lista_mixta.count(True), " veces en la lista")

##consultar el maximo y minimo de una lista numerica con max y min
lista_numerica = [3,56,23,89,2,5,78]
print("Lista numerica: ", lista_numerica)
print("mayor elemento de la lista: ", max(lista_numerica))
print("menor elemento de la lista: ", min(lista_numerica))

##ordenar una lista numerica con sort
lista_numerica.sort()
print("lista numerica ordenada: ", lista_numerica)