from book_manager import ab, vb, sb
from member_manager import am, vm
from issue_manager import ib, rb
from library_report import lb


def show_menu():
    print("\n1. Add Books")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Members")
    print("5. View Members")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Library Report")
    print("9. Exit")


def main_menu():
    print("=" * 45)
    print("    WELCOME TO LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)

    while True:
        show_menu()

        c = int(input("Enter Choice: "))

        if c == 1:
            ab()
        elif c == 2:
            vb()
        elif c == 3:
            sb()
        elif c == 4:
            am()
        elif c == 5:
            vm()
        elif c == 6:
            ib()
        elif c == 7:
            rb()
        elif c == 8:
            lb()
        elif c == 9:
            print("Thank you!")
            break
        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()
