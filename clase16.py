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
def multiplicacion_division(numeros, operadores):
    for operador in range(len(operadores)):
        if operadores[operador] in "*/":        
            if operadores[operador] == "*":
                numeros[operador+1] = numeros[operador] * numeros[operador+1]
                
            else:  #si es /
                numeros[operador+1] = numeros[operador] / numeros[operador+1]
            
            numeros[operador] = "."
            operadores[operador] = "."
    operadores.append(".") ## para que lalista deoperadores quede de igualtamaño a la de numeros
    
    return numeros, operadores


def crear_lista_final(numeros, operadores):
    lista_final = []    ##lista con los numero ya multiplicados/divididos intercalados en orden con sumas o restas
    
    for indice in range(len(numeros)):
        if numeros[indice] != ".":
            lista_final.append(numeros[indice])

        if operadores[indice] != ".":
            lista_final.append(operadores[indice])       

    return lista_final



def suma_resta(listaFinal):
    resultado_final = 0
    for indice in range(len(listaFinal)):
        if listaFinal[indice] == "+"or listaFinal[indice] =="-":
            if listaFinal[indice] == "+":
                listaFinal[indice+1] = listaFinal[indice-1] + listaFinal[indice+1]
            if listaFinal[indice] == "-":
                listaFinal[indice+1] = listaFinal[indice-1] - listaFinal[indice+1]
    resultado_final = listaFinal[-1]   ## va calculando modificando la lista hasta dejar el resultado al final del todo
    return resultado_final



def calcular(texto):
    texto = texto.replace(' ', '')
    numeros, operadores = separar_elementos(texto)
    print(f"Números iniciales: {numeros}")
    print(f"Operadores iniciales: {operadores}")

    numeros, operadores =  multiplicacion_division(numeros,operadores)
    print(f"listas sucias de: \n Numeros multi /divi: {numeros}\n Operadores suma y resta: {operadores} ")

    lista_final = crear_lista_final(numeros, operadores)
    print(f"lista limpia con numeros intercalados con sumas y restas: {lista_final}")

    resultado = suma_resta(lista_final)
    print(f"resultado de calcular {texto}:  es \n")
    return resultado


#print(calcular("3234/343+12346-875.826-345*345*345*765/22-12313-1231"))  ##vamos bien

operation=input("Por favor ingrese la operación matemática (sin paréntesis y sin exponentes)")
print(calcular(operation))

## excelente pero se rompe si el primer dígito es negativo ¿podré solucionarlo?