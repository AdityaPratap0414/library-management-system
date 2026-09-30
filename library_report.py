from book_manager import books
from member_manager import members

def lb():
    print("\n----- LIBRARY REPORT -----")

    print("Total Books:", len(books))
    print("Total Members:", len(members))

    available = 0
    issued = 0

    for i in books:
        if i["available"] == True:
            available = available + 1
        else:
            issued = issued + 1

    print("Available Books:", available)
    print("Issued Books:", issued)
