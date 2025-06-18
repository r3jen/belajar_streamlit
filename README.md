# 📚 Belajar Streamlit - Aplikasi Daftar Buku

Aplikasi web sederhana yang dibangun menggunakan Streamlit untuk mengelola daftar buku. Aplikasi ini memungkinkan pengguna untuk menambahkan buku baru dengan judul dan penulis, serta menampilkan daftar buku yang telah ditambahkan.

## 🚀 Fitur

- ✅ Menambahkan buku baru dengan judul dan penulis
- ✅ Menampilkan daftar buku yang telah ditambahkan
- ✅ Interface yang user-friendly dengan emoji
- ✅ Validasi input untuk memastikan data lengkap
- ✅ Session state untuk menyimpan data selama sesi berlangsung

## 📁 Struktur Proyek

```
belajar_streamlit/
├── app.py          # Aplikasi utama dengan semua kode dalam satu file
├── main.py         # Aplikasi yang menggunakan modul terpisah
├── utils.py        # Modul utilitas berisi class Book dan fungsi add_book
└── README.md       # Dokumentasi proyek
```

## 🛠️ Teknologi yang Digunakan

- **Streamlit**: Framework untuk membuat aplikasi web dengan Python
- **Python**: Bahasa pemrograman utama
- **Session State**: Untuk menyimpan data selama sesi aplikasi

## 📋 Prasyarat

Sebelum menjalankan aplikasi, pastikan Anda telah menginstal:

- Python 3.7 atau versi yang lebih baru
- Streamlit

## ⚙️ Instalasi

1. Clone atau download proyek ini
2. Buka terminal/command prompt di direktori proyek
3. Install dependencies:

```bash
pip install streamlit
```

## 🚀 Cara Menjalankan

### Opsi 1: Menggunakan app.py (Semua kode dalam satu file)
```bash
streamlit run app.py
```

### Opsi 2: Menggunakan main.py (Dengan modul terpisah)
```bash
streamlit run main.py
```

Setelah menjalankan perintah di atas, aplikasi akan terbuka di browser Anda dengan URL `http://localhost:8501`.

## 📖 Cara Menggunakan

1. **Menambahkan Buku Baru**:
   - Masukkan judul buku di field "Masukkan judul buku"
   - Masukkan nama penulis di field "Masukkan nama penulis"
   - Klik tombol "➕ Tambah Buku"

2. **Melihat Daftar Buku**:
   - Daftar buku akan otomatis ditampilkan di bagian bawah aplikasi
   - Setiap buku akan ditampilkan dengan format: "📖 'Judul Buku' oleh Nama Penulis"

3. **Validasi Input**:
   - Aplikasi akan memastikan kedua field (judul dan penulis) terisi sebelum menambahkan buku
   - Pesan sukses akan muncul jika buku berhasil ditambahkan
   - Pesan peringatan akan muncul jika ada field yang kosong

## 🏗️ Arsitektur Kode

### Class Book
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        return f"📖 '{self.title}' oleh {self.author}"
```

### Fungsi add_book
```python
def add_book(book_list, title, author):
    new_book = Book(title, author)
    book_list.append(new_book)
    return new_book
```

## 🔧 Perbedaan antara app.py dan main.py

- **app.py**: Berisi semua kode dalam satu file (class Book, fungsi add_book, dan aplikasi Streamlit)
- **main.py**: Menggunakan modul terpisah dengan mengimpor class dan fungsi dari `utils.py`

## 🎯 Tujuan Pembelajaran

Proyek ini dirancang untuk mempelajari:
- Dasar-dasar Streamlit
- Penggunaan session state
- Pembuatan interface web sederhana
- Pengorganisasian kode dengan modul
- Validasi input pengguna
- Penggunaan class dan fungsi dalam Python

## 🤝 Kontribusi

Silakan berkontribusi dengan:
- Melaporkan bug
- Menyarankan fitur baru
- Membuat pull request

## 📝 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran dan dapat digunakan secara bebas.

## 👨‍💻 Pengembang

Dibuat sebagai bagian dari pembelajaran Streamlit.

---

**Selamat belajar Streamlit! 🎉**