#  Manejo de errores y excepciones ##
def ingresar_datos():
    nombre = input("Ingesa tu nombre de usuario")
    edad = int(input("ingresa tu edad"))
    return nombre,edad
     

# la sintaxis es: (el while true es olopara que lo intente hasta que no haya error)
try:
    nombre1, edad1 = ingresar_datos()
    
except ValueError:
    print("Número no válido, por favor ingrese un entero válido")
    
## codigo que imprime todlas excepciones y susclasificaciones ##
def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)