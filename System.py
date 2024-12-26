import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Establish a connection to the MySQL database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="me",  # Replace with your username
        password="mido122mido",  # Replace with your password
        database="LibraryManagement"
    )

# Function to fetch books from the database
def fetch_books():
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Books")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return []

# Function to add a book to the database
def add_book(title, author, genre, isbn, year, copies):
    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Books (Title, Author, Genre, ISBN, PublishedYear, CopiesAvailable) VALUES (%s, %s, %s, %s, %s, %s)",
            (title, author, genre, isbn, year, copies)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Book added successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# GUI application class
class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x600")

        # Frame for book information
        book_frame = ttk.LabelFrame(self.root, text="Book Management")
        book_frame.pack(fill="x", padx=10, pady=10)

        # Book information labels and entries
        ttk.Label(book_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry = ttk.Entry(book_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(book_frame, text="Author:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.author_entry = ttk.Entry(book_frame, width=30)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(book_frame, text="Genre:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.genre_entry = ttk.Entry(book_frame, width=30)
        self.genre_entry.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(book_frame, text="ISBN:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.isbn_entry = ttk.Entry(book_frame, width=30)
        self.isbn_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(book_frame, text="Published Year:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.year_entry = ttk.Entry(book_frame, width=30)
        self.year_entry.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(book_frame, text="Copies Available:").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.copies_entry = ttk.Entry(book_frame, width=30)
        self.copies_entry.grid(row=5, column=1, padx=5, pady=5)

        # Add book button
        add_book_button = ttk.Button(book_frame, text="Add Book", command=self.add_book)
        add_book_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Frame for book list
        list_frame = ttk.LabelFrame(self.root, text="Books List")
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Book list treeview
        columns = ("BookID", "Title", "Author", "Genre", "ISBN", "PublishedYear", "CopiesAvailable")
        self.book_tree = ttk.Treeview(list_frame, columns=columns, show="headings")
        for col in columns:
            self.book_tree.heading(col, text=col)
            self.book_tree.column(col, width=100)
        self.book_tree.pack(fill="both", expand=True)

        # Load books into the treeview
        self.load_books()

    def load_books(self):
        for row in self.book_tree.get_children():
            self.book_tree.delete(row)
        books = fetch_books()
        for book in books:
            self.book_tree.insert("", "end", values=book)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        isbn = self.isbn_entry.get()
        year = self.year_entry.get()
        copies = self.copies_entry.get()

        if not all([title, author, genre, isbn, year, copies]):
            messagebox.showerror("Input Error", "All fields are required!")
            return

        add_book(title, author, genre, isbn, year, copies)
        self.load_books()

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
