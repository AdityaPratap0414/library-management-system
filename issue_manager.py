from book_manager import books
from member_manager import members

def ib():  # Issue Books
    if len(books) == 0:
        print("No Book available!")
    elif len(members) == 0:
        print("No Member found!")
    else:
        mid = input("Enter Member ID: ")

        member_found = False

        for m in members:
            if m["id"] == mid:
                member_found = True

        if member_found == False:
            print("Member not found!")
            return

        uid = input("Enter Book ID: ")

        for i in books:
            if i["id"] == uid:
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
