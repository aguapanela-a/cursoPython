#Diccionarios en Python: Uso y Manipulación de Datos
keys={
    "w": "up",
    "a": "left",
    "s": "down",
    "d": "rigth",
    "eliminado": "elominado"
}

print(keys["w"])
print(keys)

#eliminar una clave
del keys["eliminado"]

#imprime solo las claves
claves = keys.keys()
print(claves)

#imprime solo los valores
valores = keys.values()
print(valores)

#imprime tanto claves como valores
pares = keys.items()
print(pares)

##diccionario de diccionarios
lista_contactos = {
    "juan":{
        "apellido": "Jimenez",
        "edad": 21,
        "educación": "Superior"
    },
    "nikolas":{
        "apellido": "Castro",
        "edad": 23,
        "educación": "Superior"
    },
    "miguel":{
        "apellido": "Audelo",
        "edad": 22,
        "educación": "Superior"
    }
}
print(lista_contactos["miguel"])

##otros ojemplos:
###e-commerce con info de productos
### info de clientes
### info de cifras 

## lista de contactos en formato json.
import json
json_data = json.dumps(lista_contactos)
print("Datos en json: ", json_data)