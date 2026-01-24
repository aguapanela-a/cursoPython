# crear consecionaria de vehículos
# se podrá hacer compra y venta
# dónde los usuarios pueden combrar vehiculos, vender, cuales están disponibles, precios

import string
import random
class User:
    def __init__(self, name, user_id, mail):
        self.name = name
        self.user_id = user_id
        self.mail = mail
        self.length_of_string = 10
        self.password = "".join( #un string.join() lo que hace es unir una lista de caracteres en un string
            random.SystemRandom().choice(string.ascii_letters + string.digits) #elige un caracter aleatorio de letras mayusculas, minusculas y digitos
            for _ in range(self.length_of_string) #para cada uno en el rango de la longitud del string
        ) #finalmente genera una contraseña aleatoria de 10 caracteres
        
        self.vehicles = []
        
    
    def buy_car(self, car):
        pass #ejecuta el método vender vehiculo de la consecionaria
    
    def sell_car(self, car):
        pass #ejecuta el método comprar vehiculo de la consecionaria
    
    def show_vehicles(self):
        print(f"Vehículos de {self.name}:")
        for vehicle in self.vehicles:
            print(f"  - {vehicle}")
        
    def view_vehicles(self):
        pass #Ejecuta el método mostrar vehiculos disponibles de la consesionaria

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.is_available = True

class Concessionaire:
    pass