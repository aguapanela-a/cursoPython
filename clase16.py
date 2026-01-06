## funciones y parámetros en python ##
## calculadora ##
def separar_elementos(texto): ## 34*34/4
    numero_actual = ""
    numeros  = []
    operadores = []
    
    for char in texto:
        if char not in ["+","-","*","/"]:
            numero_actual += char
        
        else:
            operadores.append(char)
            numero_entero = int(numero_actual)
            numeros.append(numero_entero)
            numero_actual = ""
    return numeros, operadores

prueba1 = separar_elementos("21*34+999/666")
print(prueba1)
### No agarra después del "/" el 666 ###

            
        





def calculadora():
    while True:
        operacion = input("Ingrese la operación") ## 34*56+46
        for char in operacion:
            if char in ["+","-","*","/"]:
                pass