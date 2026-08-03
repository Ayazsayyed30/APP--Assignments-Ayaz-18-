class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Patron:
    def __init__(self, name: str, patron_id: str):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def __str__(self):
        return f"Patron: {self.name} (ID: {self.patron_id})"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book: Book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            return True
        return False

    def register_patron(self, patron: Patron):
        if patron.patron_id not in self.patrons:
            self.patrons[patron.patron_id] = patron
            return True
        return False

    def borrow_book(self, patron_id: str, isbn: str) -> bool:
        if patron_id in self.patrons and isbn in self.books:
            patron = self.patrons[patron_id]
            book = self.books[isbn]
            
            if not book.is_borrowed:
                book.is_borrowed = True
                patron.borrowed_books.append(book)
                return True
        return False

    def return_book(self, patron_id: str, isbn: str) -> bool:
        if patron_id in self.patrons and isbn in self.books:
            patron = self.patrons[patron_id]
            book = self.books[isbn]
            
            if book in patron.borrowed_books:
                book.is_borrowed = False
                patron.borrowed_books.remove(book)
                return True
        return False

    def display_books(self):
        for book in self.books.values():
            print(book)


if __name__ == "__main__":
    my_library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("1984", "George Orwell", "9780451524935")
    
    my_library.add_book(book1)
    my_library.add_book(book2)

    patron1 = Patron("Alice Smith", "P001")
    my_library.register_patron(patron1)

    my_library.borrow_book("P001", "9780743273565")
    
    my_library.return_book("P001", "9780743273565")


