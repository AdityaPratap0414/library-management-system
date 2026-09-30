# Library Management System

A simple command-line library program written in Python.
Made for the **Python Essentials** course (VITyarthi) - Build Your Own Project.

**Name:** Aditya Pratap Singh
**Register Number:** 26BCE10793

## About

This program helps a small library manage its books and members. The user picks an option from a numbered menu, and the program shows the result and returns to the menu.

## Features

1. Add Books - enter book ID, title and author
2. View Books - list all books and whether each is available
3. Search Book - find a book by its Book ID
4. Add Members - enter member ID and name
5. View Members - list all members
6. Issue Book - enter the book ID to issue it
7. Return Book - enter the book ID to return it
8. Library Report - total, available and issued books, and total members
9. Exit

## Project Files

| File | Purpose |
|------|---------|
| main.py | Shows the welcome message and menu, and calls the other files |
| book_manager.py | Add, view and search books |
| member_manager.py | Add and view members |
| issue_manager.py | Issue and return books |
| library_report.py | Library report |

## Requirements

- Python 3 (the program uses only the standard library)

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```
python main.py
```

4. Type a menu number and press Enter.

## Sample Run

```
1. Add Books
2. View Books
3. Search Book
4. Add Members
5. View Members
6. Issue Book
7. Return Book
8. Library Report
9. Exit
Enter Choice: 1
Enter Book ID: 101
Enter Book Title: CSE
Enter Book Author: KANNAN S
Books added successfully!
```

## Note

Data is stored in lists while the program runs, so it is cleared when the program is closed.

## Concepts Used

- Functions and modules
- Lists and dictionaries
- Loops and conditions
- Menu-driven program

## Future Improvements

- Save data so it is not lost when the program closes
- Check the member ID when issuing a book
- Due dates and fines for late returns
- Better input checking
- Login for users
