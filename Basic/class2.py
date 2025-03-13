
class Book:
    total_books=0
    def __init__(self, title, author, isbn):
        self.title= title
        self.author= author
        self.isbn =isbn
        Book.total_books+=1

    def update_title(self, new_title):
        self.title = new_title

    def update_author(self,new_author):
        self.author = new_author        

    def display_info(self, user_type="reader"):
        if user_type=="librarian":
            print(f"Title: {self.title}, Author: {self.author}, ISBN : {self.isbn}")
        else:
            print(f"Title: {self.title}, Author: {self.author}")
        
    @staticmethod
    def book_info():
        print("Books are foundation of education")
        
    @classmethod
    def get_total_books(cls):
        return cls.total_books    



class Author:
    total_authors=0

    def __init__(self,name,birthdate):
        self.name= name
        self.birthdate= birthdate
        self.books=[]
        Author.total_authors+=1

    def add_books(self,book):
        self.books.append(book)
    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                Book.total_books-=1
                print(f"book with {isbn} removed author named : {self.name}")    
                return print("Book is not available")
            
    @staticmethod
    def author_info():
        print("Authors are content creator")

    @classmethod
    def get_total_authors(cls):
        return cls.total_authors    
    


class Library:
    library_count=0

    def __init__(self):
        self.books=[]
        self.authors=[]
        Library.library_count +=1 

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                Book.total_books-=1
                print(f"book with {isbn} removed author named : {self.name}")    
                return print("Book is not available")

    def list_books(self):
        for book in self.books:
            print(f"Title : {book.title}, Author : {book.author}, ISBN: {book.isbn}")

    @classmethod
    def get_library_count(cls):
        return cls.library_count

    @staticmethod
    def library_info():
        print("Library is access to books and authors")
                   


book1 = Book("Java programming","abc","123123123")
book2 = Book("Python Programming","pqr","456456456")

author1 = Author("abc","1900-01-01")
author1.add_books(book1)

library = Library()
library.add_book(book1)
library.add_book(book2)

library.list_books()

book1.update_title("Advanced java prog.")
book1.display_info("librarian")

print("Total Books : ",Book.get_total_books())
print("Total Authors : ",Author.get_total_authors())
print("Total Libraries : ",Library.get_library_count())

Library.library_info()
Book.book_info()
Author.author_info()
