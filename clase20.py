## POO EN PYTHON ##
# # las clases son una plantilla con la que instanciarán objetos con esos atributos (variables) y métodos (funciones)

## Creao la calse tipo Persona:
class Person:   
    def __init__(self, name, age): ## definir el constructor: Lo que se hace aquí es definir qué atributos principales  tomará cualquier objeto de tipo persona
        self.name = name
        self.age = age
        
    def greet(self, user):  ## definir un método: esto serán las funciones que todos los objetos de tipo ´persona harám , por ejemplo todos pódrán saludar
        saludo = f"Hello {user}, my name is {self.name}, and i am {self.age} years old"
        return saludo
    

persona1 = Person("Erick", 20) ## crear un opbjeto persona1 de tipo Person
persona2 = Person("Laura", 25)

usuario = input("Por favorn ingrese su nombre de usuario: ")

print(persona1.greet(usuario))