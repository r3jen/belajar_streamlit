import streamlit as st

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

# --- Streamlit App ---
st.title("📚 Daftar Buku Sederhana")

# Inisialisasi session state untuk menyimpan daftar buku
if 'book_list' not in st.session_state:
    st.session_state.book_list = []

# Input dari pengguna
title_input = st.text_input("Masukkan judul buku:")
author_input = st.text_input("Masukkan nama penulis:")

# Tombol tambah buku
if st.button("➕ Tambah Buku"):
    if title_input and author_input:
        book = add_book(st.session_state.book_list, title_input, author_input)
        st.success(f"Buku berhasil ditambahkan: {book.describe()}")
    else:
        st.warning("Harap isi judul dan penulis buku!")

# Menampilkan daftar buku
st.subheader("📖 Daftar Buku:")
if st.session_state.book_list:
    for idx, book in enumerate(st.session_state.book_list, start=1):
        st.write(f"{idx}. {book.describe()}")
else:
    st.write("Belum ada buku yang ditambahkan.")
