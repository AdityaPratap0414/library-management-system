from book_manager import add_book, view_books, search_books 
from member_manager import add_member, view_members 
from issue_manager import issue_book, return_book 
from reports import library_report 
from database import load_data, save_data 
from validation import get_menu_choice 


def show_menu(): 
    print("\n1. Add Book\n2. View Books\n3. Search Book\n4. Add Member\n5. View Members\n6. Issue Book\n7. Return Book\n8. Library Report\n9. Exit") 


def main(): 
    books, members = load_data() 

    print("=" * 45) 
    print("    WELCOME TO LIBRARY MANAGEMENT SYSTEM") 
    print("=" * 45) 

    while True: 
        show_menu() 
        choice = get_menu_choice(1, 9) 

        if choice == 1: 
            add_book(books) 
        elif choice == 2: 
            view_books(books) 
        elif choice == 3: 
            search_books(books) 
        elif choice == 4: 
            add_member(members) 
        elif choice == 5: 
            view_members(members) 
        elif choice == 6: 
            issue_book(books, members) 
        elif choice == 7: 
            return_book(books) 
        elif choice == 8: 
            library_report(books, members) 
        else: 
            save_data(books, members) 
            print("Thank you!") 
            break 


if __name__ == "__main__": 
    main() 
