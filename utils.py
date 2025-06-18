# utils.py

# --- Class Buku ---
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"📖 '{self.title}' oleh {self.author}"

# --- Fungsi Tambah Buku ---
def add_book(book_list, title, author):
    new_book = Book(title, author)
    book_list.append(new_book)
    return new_book
