import random
import math
from datetime import datetime, timedelta
from functools import reduce

# -----------------------------
# Book Class
# -----------------------------
class Book:
    def __init__(self, title, author):
        self.__id = random.randint(1000, 9999)
        self.__title = title.title()
        self.__author = author.title()
        self.__is_issued = False
        self.__due_date = None

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_issued(self):
        return self.__is_issued

    def issue(self):
        self.__is_issued = True
        self.__due_date = datetime.now() + timedelta(days=7)

    def return_book(self):
        fine = 0
        if self.__due_date and datetime.now() > self.__due_date:
            late_days = (datetime.now() - self.__due_date).days
            fine = math.ceil(late_days * 2)
        self.__is_issued = False
        self.__due_date = None
        return fine

    def __str__(self):
        status = "Issued" if self.__is_issued else "Available"
        return f"ID: {self.__id}, {self.__title} by {self.__author} ({status})"


# -----------------------------
# Member Class
# -----------------------------
class Member:
    def __init__(self, name):
        self.__id = random.randint(100, 999)
        self.__name = name.title()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Member ID: {self.__id}, Name: {self.__name}"


# -----------------------------
# Library Class
# -----------------------------
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.issued_books = set()
        self.transactions = []

    # CRUD Operations
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("Book Added Successfully")

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        print("Member Added Successfully")

    def remove_book(self, book_id):
        self.books = list(filter(lambda b: b.get_id() != book_id, self.books))

    # Recursive Search
    def search_book_recursive(self, title, index=0):
        if index >= len(self.books):
            return None
        if title.lower() in self.books[index].get_title().lower():
            return self.books[index]
        return self.search_book_recursive(title, index + 1)

    # Issue Book
    def issue_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id and not book.is_issued():
                book.issue()
                self.issued_books.add(book_id)
                self.transactions.append(("ISSUE", book_id, datetime.now()))
                print("Book Issued Successfully")
                return
        print("Book not available")

    # Return Book
    def return_book(self, book_id):
        for book in self.books:
            if book.get_id() == book_id and book.is_issued():
                fine = book.return_book()
                self.issued_books.remove(book_id)
                self.transactions.append(("RETURN", book_id, datetime.now()))
                print(f"Book Returned. Fine: ₹{fine}")
                return
        print("Invalid Book ID")

    # Functional Programming Example
    def count_issued_books(self):
        return reduce(lambda x, _: x + 1, self.issued_books, 0)

    # File Persistence
    def save_data(self):
        with open("books.txt", "w") as f:
            for book in self.books:
                f.write(str(book) + "\n")

    def load_data(self):
        try:
            with open("books.txt", "r") as f:
                print("\nSaved Books:")
                print(f.read())
        except FileNotFoundError:
            print("No saved data found.")


# -----------------------------
# Menu System
# -----------------------------
def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Count Issued Books")
        print("7. Save Data")
        print("8. Load Data")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter Member Name: ")
            library.add_member(name)

        elif choice == "3":
            title = input("Enter Title to Search: ")
            book = library.search_book_recursive(title)
            print(book if book else "Book not found")

        elif choice == "4":
            book_id = int(input("Enter Book ID: "))
            library.issue_book(book_id)

        elif choice == "5":
            book_id = int(input("Enter Book ID: "))
            library.return_book(book_id)

        elif choice == "6":
            print("Total Issued Books:", library.count_issued_books())

        elif choice == "7":
            library.save_data()

        elif choice == "8":
            library.load_data()

        elif choice == "9":
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
