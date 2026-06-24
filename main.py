books = []

while True:
    print("\n========================")
    print("LIBRARY MANAGEMENT SYSTEM")
    print("========================")

    print("1. Add Book")
    print("2. Show Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    option = input("Choose an option: ")

    # =======================
    # ADD BOOK
    # =======================
    if option == "1":
        title = input("Book title: ")
        author = input("Author: ")
        year = input("Year: ")

        book = {
            "title": title,
            "author": author,
            "year": year
        }

        books.append(book)
        print("Book added successfully!")

    # =======================
    # SHOW BOOKS
    # =======================
    elif option == "2":
        print("\n=== BOOK LIST ===")

        if len(books) == 0:
            print("No books available.")
        else:
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book['title']} - {book['author']} ({book['year']})")

    # =======================
    # SEARCH BOOK
    # =======================
    elif option == "3":
        search = input("Enter book title: ")
        found = False

        for book in books:
            if book["title"].lower() == search.lower():
                print("\nBook found:")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Year: {book['year']}")
                found = True
                break

        if not found:
            print("Book not found.")

    # =======================
    # DELETE BOOK
    # =======================
    elif option == "4":
        delete = input("Enter book title to delete: ")
        found = False

        for book in books:
            if book["title"].lower() == delete.lower():
                books.remove(book)
                print("Book deleted successfully.")
                found = True
                break

        if not found:
            print("Book not found.")

    # =======================
    # EXIT
    # =======================
    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
        