class Book:
    """A class representing a book with a title and an author."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"The book '{title}' has been checked out."
        return f"The book '{title}' is either not available or does not exist in the library."
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"The book '{title}' has been returned."
        return f"The book '{title}' is either not checked out or does not exist in the library."
    
    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books in the library.")

# main.py for testing
from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    print("\n" + library.check_out_book("1984"))
    print("Available books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    print("\n" + library.return_book("1984"))
    print("Available books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
