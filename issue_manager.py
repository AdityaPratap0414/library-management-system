from book_manager import books

def ib():  # Issue Books
    if len(books) == 0:
        print("No Book available!")
    else:
        uid = input("Enter Book ID: ")

        for i in books:
            if uid == i["id"]:
                if i["available"] == True:
                    i["available"] = False
                    print("Book Issued successfully!")
                else:
                    print("Book is already issued!")
                return

        print("Book not found!")


def rb():  # Return Books
    if len(books) == 0:
        print("No Book found!")
    else:
        uid = input("Enter Book ID: ")

        for i in books:
            if i["id"] == uid:
                if i["available"] == False:
                    i["available"] = True
                    print("Book Returned successfully")
                else:
                    print("Book was not issued")
                return

        print("Book not found!")
