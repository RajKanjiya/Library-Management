import os
from functions.getBooks import get_book, get_all_books
from functions.searchBook import search_book
from functions.addNewBook import add_book
from functions.updateBook import update_book


def clear_terminal():
    # Check the operating system name
    if os.name == 'nt':
        # For Windows, use 'cls' command
        _ = os.system('cls')
    else:
        # For Linux, macOS, and other POSIX systems, use 'clear' command
        _ = os.system('clear')

books = {
    '1': {
        'Title': 'Bhagwat Geeta',
        'Author': 'Shree Krishna',
        'Year': 0,
        'copies' : 10
    },
    '2': {
        'Title': 'To Kill a Mockingbird',
        'Author': 'Harper Lee',
        'Year': 1960,
        'copies' : 10
    },
    '3': {
        'Title': 'The Great Gatsby',
        'Author': 'F. Scott Fitzgerald',
        'Year': 1925,
        'copies' : 10
    },
    '4': {
        'Title': 'Pride and Prejudice',
        'Author': 'Jane Austen',
        'Year': 1813,
        'copies' : 10
    },
    '5': {
        'Title': 'The Hobbit',
        'Author': 'J.R.R. Tolkien',
        'Year': 1937,
        'copies': 10
    },
    '6': {
        'Title': 'The Catcher in the Rye',
        'Author': 'J.D. Salinger',
        'Year': 1951,
        'copies': 10
    },
    '7': {
        'Title': 'Fahrenheit 451',
        'Author': 'Ray Bradbury',
        'Year': 1953,
        'copies': 10
    },
    '8': {
        'Title': 'Moby-Dick',
        'Author': 'Herman Melville',
        'Year': 1851,
        'copies': 10
    },
    '9': {
        'Title': 'The Alchemist',
        'Author': 'Paulo Coelho',
        'Year': 1988,
        'copies': 10
    },
    '10': {
        'Title': 'Harry Potter and the Philosopher\'s Stone',
        'Author': 'J.K. Rowling',
        'Year': 1997,
        'copies': 10
    }
}

while 1:
    print("1. Add new Book\n2. Display book by Book_id\n3. Display All books\n4. Search book by book name\n5. Update Book\n6. Exit")
    c = int(input('Enter Your Choice:--'))

    match c:
        case 1:
            print("Enter Book Details ID , Title , Author , Year , Copies")
            id = input()
            title = input()
            author = input()
            year = int(input())
            copies = input()
            add_book(id , title , author , year , copies , books)

        case 2:
            clear_terminal()
            id = input("Enter Book ID:--")
            get_book(id , books)

        case 3:
            clear_terminal()
            get_all_books(books)

        case 4:
            clear_terminal()
            book_name = input("Enter book name :-")
            book_name = book_name.lower()
            search_book(book_name , books)

        case 5:
            clear_terminal()
            book_name = input("Enter book name :-")
            book_name = book_name.lower()
            update_book(book_name, books)

        case 6:
            print("Exit")
            clear_terminal()
            break