## RECUIRSIVIDAD ##
def factorial(x): #4! = 4*3!
                     #3! = 3 * 2!
  if x == 0:
    return 1
  else:
    re = x * factorial(x-1)
  return re

print(factorial(5))
## siempre hay que definir el caso base, el caso que detendrá la recursividad, en este caso deja de llamarse a simisma la función solo cuando x == 0, y unicamente retornará un 1

## fibonacci
def fibonacci(nivel):
  if  nivel == 0:
    return 0
  elif nivel == 1:
    return 1
  else:
    return fibonacci(nivel-1) + fibonacci(nivel-2)
  
print("fibonacci: ",fibonacci(30))


## función sumatoria 4 = 4+3+2+1   =   

def sumtoria(x):
  if x == 1:
    return 1
  else:
    return x + sumtoria(x-1)

print(sumtoria(5))


### DEBO PRACTICAR VARIOS EJERCICIOS DE RECURSIVIDAD ####