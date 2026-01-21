## POO EN PYTHON: bibioteca ejercicio ##

#libro tendrá autor y título
#persona que va a poder pedir prestado un libro o devolver
#biblioteca gestioionará libros y usuarios

#poner excepción de escribir un numero no un str en copies
class User:
    def __init__(self, name, user_id):
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