## POO EN PYTHON: bibioteca ejercicio ##

#libro tendrá autor y título
#persona que va a poder pedir prestado un libro o devolver
#biblioteca gestioionará libros y usuarios

#poner excepción de escribir un numero no un str en copies
class User:
    def __init__(self, name, user_id = int):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def borrow_book(self, book): 
        if book.borrow_():
            self.borrowed_books.append(book)
        
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_()
            self.borrowed_books.remove(book)
        else:
            print(f"bro... No puedes devolver el libro {book.title} porque no lo tienes gran pendejo")
    
    def get_borrowed_books(self):
        print(f"{self.name} tiene los sigueintes libros:")
        for book in self.borrowed_books:
            print(f"    - {book.title}")
        
            
        

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.available = True
    
    def borrow_(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
            return True
        else:
            print(f"el libro {self.title} no está disponible en este momento")
            return False
            
    def return_(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")
        
        
class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_books(self, book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido añadido")
        
    def register_user(self, user):
        self.users.append(user)
        print(f"EL usuario {user.name} ha sido registrado")
    
    def get_available_books(self):
        print("Libros de biblioteca central")
        for book in self.books:
            if book.available:
                print(f"   - {book.title} por {book.author}. Estado: Disponible")
            else:
                print(f"   - {book.title} por {book.author}. Estado: No disponible")
           
 ### creación de objetos ###
 
juan = User("Juan", 1)
maria = User("maria", 2)
carlos = User("carlos", 3)
mario = User("mario", 4)

libro1 = Book("Jhon Katzenbach", "El Psicoanalista")
libro2 = Book("M. Ryzl", "Como potenciar sus poderes paranormales")
libro3 = Book("Kynney", "El diario de Greg")
libro4 = Book("Karen McCombie", "Por amor...")
libro5 = Book("Stephen King", "Maleficio")
libro6 = Book("Sergio Camargo V.", "El narcotraficante N° 82 Álvaro Uribe Vélez Presidente de Colombia")

bibliotecaCentral = Library()
bibliotecaCentral.add_books(libro1)
bibliotecaCentral.add_books(libro2)
bibliotecaCentral.add_books(libro3)
bibliotecaCentral.add_books(libro4)
bibliotecaCentral.add_books(libro5)
bibliotecaCentral.add_books(libro6)

bibliotecaCentral.register_user(juan)
bibliotecaCentral.register_user(maria)
bibliotecaCentral.register_user(carlos)
bibliotecaCentral.register_user(mario)


bibliotecaCentral.get_available_books()

juan.borrow_book(libro1)
juan.borrow_book(libro4)
juan.borrow_book(libro6)

maria.borrow_book(libro1)
maria.borrow_book(libro2)

bibliotecaCentral.get_available_books()

juan.get_borrowed_books()
maria.get_borrowed_books()

juan.return_book(libro4)

bibliotecaCentral.get_available_books()
