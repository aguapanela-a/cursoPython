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
            numero_flotante = float(numero_actual)
            numeros.append(numero_flotante)
            numero_actual = ""
    
    numeros.append(float(numero_actual))
    return numeros, operadores


## ya sepaa bien los números y agarra los operadores

## Aplicar PEMDAS (paréntesis, exponentes,multiplicación, división, adición y substracción)
#primero * y / lueg + y -
def calcular(texto):
    numeros, operadores = separar_elementos(texto)
    print(f"Números: {numeros}")
    print(f"Operadores: {operadores}")

    lista_final = []
    
    for operador in range(len(operadores)):
        if operadores[operador] in "*/":        
            if operadores[operador] == "*":
                numeros[operador+1] = numeros[operador] * numeros[operador+1]
                
            else:  #si es /
                numeros[operador+1] = numeros[operador] / numeros[operador+1]
            
            numeros[operador] = "."
            operadores[operador] = "."
    
    ### FALTA PONER EN UNA LISTA NUMEROS Y OPERADORES INTERCALADOS ##
        
    return numeros, operadores

print(calcular("21-34+999/666/75/454*1342+1234"))  ##vamos bien


            




def calculadora():
    while True:
        operacion = input("Ingrese la operación") ## 34*56+46
        for char in operacion:
            if char in ["+","-","*","/"]:
                pass