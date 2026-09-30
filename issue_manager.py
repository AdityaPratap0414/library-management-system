def issue_book(books, members):
    book_id = input("Enter Book ID: ")
    member_id = input("Enter Member ID: ")

    book = None
    member = None

    for item in books:
        if item["id"] == book_id:
            book = item
            break

    for item in members:
        if item["id"] == member_id:
            member = item
            break

    if book is None:
        print("Book not found.")
        return

    if member is None:
        print("Member not found.")
        return

    if not book["available"]:
        print("Book is already issued.")
        return

    book["available"] = False
    book["issued_to"] = member_id
    print("Book issued successfully.")


def return_book(books):
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                print("Book is already available.")
                return

            book["available"] = True
            book["issued_to"] = None
            print("Book returned successfully.")
            return

    print("Book not found.")
