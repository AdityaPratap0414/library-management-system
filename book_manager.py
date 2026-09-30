books = []

def ab():  # Add Books
    id = input("Enter Book ID: ")
    t = input("Enter Book Title: ")
    a = input("Enter Book Author: ")

    books.append({
        "id": id,
        "title": t,
        "author": a,
        "available": True
    })

    print("Books added successfully!")


def vb():  # View Books
    if len(books) == 0:
        print("No Book found!")
    else:
        for i in books:
            print(f'ID: {i["id"]} | Title: {i["title"]} | Author: {i["author"]} | Available: {i["available"]}')


def sb():  # Search Books
    if len(books) == 0:
        print("No Book found!")
    else:
        uid = input("Enter Book ID to search: ")

        for i in books:
            if i["id"] == uid:
                print(f'ID: {i["id"]} | Title: {i["title"]} | Author: {i["author"]} | Available: {i["available"]}')
                return

        print("Book not found!")
