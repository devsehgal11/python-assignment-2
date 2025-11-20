# Name: Dev Sehgal
# Date: 19 November, 2025
# Project Title: Library Management System



import csv
import os

# create data dictionary

books = {}
borrowed = {}

# csv data files

BOOKS_FILE = "books.csv"
BORROWED_FILE = "borrowed.csv"

# load books

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return
    with open(BOOKS_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            book_id, title, author, copies = row
            books[book_id] = {
                "title": title,
                "author": author,
                "copies": int(copies)
            }

# save books

def save_books():
    with open(BOOKS_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for book_id, data in books.items():
            writer.writerow([book_id, data["title"], data["author"], data["copies"]])

# load borrowed books

def load_borrowed():
    if not os.path.exists(BORROWED_FILE):
        return
    with open(BORROWED_FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            student, book_id = row
            borrowed[student] = book_id

# save borrowed books

def save_borrowed():
    with open(BORROWED_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        for student, book_id in borrowed.items():
            writer.writerow([student, book_id])

# add books

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Number of Copies: "))

    books[book_id] = {"title": title, "author": author, "copies": copies}
    save_books()

    print("\nBook added successfully!\n")

# view books

def view_books():
    print("\n--- BOOK LIST ---")
    print(f"{'ID':<10} {'TITLE':<20} {'AUTHOR':<20} {'COPIES':<5}")
    print("-" * 60)

    for bid, data in books.items():
        print(f"{bid:<10} {data['title']:<20} {data['author']:<20} {data['copies']:<5}")

    print()

# search for books

def search_book():
    print("\nSearch by:\n1. Book ID\n2. Title")
    choice = input("Select option: ")

    if choice == "1":
        bid = input("Enter Book ID: ")
        if bid in books:
            print("Book Found:", books[bid])
        else:
            print("Book Not Found")

    elif choice == "2":
        title = input("Enter part of title: ").lower()
        found = False
        for bid, data in books.items():
            if title in data["title"].lower():
                print(f"Found: {bid} -> {data}")
                found = True
        if not found:
            print("Book Not Found")

    else:
        print("Invalid option")

# borrow book

def borrow_book():
    student = input("Enter Student Name: ")
    bid = input("Enter Book ID to Borrow: ")

    if bid not in books:
        print("Book does not exist!")
        return

    if books[bid]["copies"] <= 0:
        print("No copies available.")
        return

    books[bid]["copies"] -= 1
    borrowed[student] = bid

    save_books()
    save_borrowed()

    print(f"\n{student} borrowed {bid} successfully!\n")

# return book

def return_book():
    student = input("Enter Student Name: ")
    
    if student not in borrowed:
        print("This student has not borrowed any book!")
        return

    bid = borrowed[student]
    books[bid]["copies"] += 1

    del borrowed[student]

    save_books()
    save_borrowed()

    print("\nBook returned successfully!\n")

    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    print("Borrowed List:", borrowed_list)

# load data

def main():
    load_books()
    load_borrowed()

    # main menu

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        ch = input("Choose an option: ")

        if ch == "1":
            add_book()
        elif ch == "2":
            view_books()
        elif ch == "3":
            search_book()
        elif ch == "4":
            borrow_book()
        elif ch == "5":
            return_book()
        elif ch == "6":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
