def add_book(books):
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")

    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True,
        "issued_to": None
    })

    print("Book added successfully.")


def view_books(books):
    if not books:
        print("No books found.")
        return

    for book in books:
        status = "Available" if book["available"] else "Issued"
        print(f'ID: {book["id"]} | Title: {book["title"]} | Author: {book["author"]} | Status: {status}')


def search_books(books):
    search = input("Enter book title or author: ").lower()
    found = False

    for book in books:
        if search in book["title"].lower() or search in book["author"].lower():
            status = "Available" if book["available"] else "Issued"
            print(f'ID: {book["id"]} | Title: {book["title"]} | Author: {book["author"]} | Status: {status}')
            found = True

    if not found:
        print("Book not found.")
