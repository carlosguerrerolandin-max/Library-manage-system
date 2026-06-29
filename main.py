# ==============================================================================
# PROYECTO INTEGRADO: BIBLIOSHARE - SISTEMA DE GESTIÓN BIBLIOTECARIA COMUNITARIA
# ==============================================================================
import json
import os

# Nombre del archivo donde se guardarán los datos permanentemente
DATABASE_FILE = "biblioteca.json"

def load_data():
    """Carga los libros desde el archivo JSON si existe; si no, devuelve una lista vacía."""
    if not os.path.exists(DATABASE_FILE):
        return []
    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        # Si el archivo está corrupto o vacío, retorna una lista vacía
        return []

def save_data(books_list):
    """Guarda la lista de libros actual en el archivo JSON."""
    try:
        with open(DATABASE_FILE, "w", encoding="utf-8") as file:
            json.dump(books_list, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def show_menu():
    print("\n========================")
    print("   BIBLIOSHARE SYSTEM   ")
    print("========================")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

def add_book(books_list):
    print("\n--- ADD NEW BOOK ---")
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    year = input("Year: ").strip()

    if not title or not author or not year:
        print("Error: All fields are required.")
        return

    book = {
        "title": title,
        "author": author,
        "year": year
    }
    books_list.append(book)
    save_data(books_list)  # <--- Guardamos los cambios en el archivo
    print(f"Success: '{title}' added successfully!")

def show_books(books_list):
    print("\n=== COMMUNITY BOOK LIST ===")
    if len(books_list) == 0:
        print("No books available in the repository yet.")
    else:
        for i, book in enumerate(books_list, start=1):
            print(f"{i}. {book['title']} - {book['author']} ({book['year']})")

def search_book(books_list):
    print("\n--- SEARCH REPOSITORY ---")
    search = input("Enter book title to search: ").strip().lower()
    found = False

    for book in books_list:
        if book["title"].lower() == search:
            print("\n[Book Found]")
            print(f"Title:  {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year:   {book['year']}")
            found = True
            break

    if not found:
        print("Result: Book not found in this library.")

def delete_book(books_list):
    print("\n--- DELETE FROM INVENTORY ---")
    delete = input("Enter book title to delete: ").strip().lower()
    found = False

    for book in books_list:
        if book["title"].lower() == delete:
            books_list.remove(book)
            save_data(books_list)  # <--- Guardamos los cambios tras eliminar
            print(f"Success: '{book['title']}' has been removed.")
            found = True
            break

    if not found:
        print("Result: Book not found. No action taken.")

def main():
    # Cargamos los libros guardados al iniciar el programa
    books = load_data()
    
    while True:
        show_menu()
        option = input("Choose an option: ").strip()

        if option == "1":
            add_book(books)
        elif option == "2":
            show_books(books)
        elif option == "3":
            search_book(books)
        elif option == "4":
            delete_book(books)
        elif option == "5":
            print("Exiting system. Thank you for supporting community education!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()