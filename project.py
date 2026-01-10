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


def add_book(book_id , title , author , year , copies):
    if(book_id in books):
        print(f"This book ID is already exist")
        return

    books[book_id] = {
        'Title' : title,
        'Author' : author,
        'Year' : year,
        'Copies' : copies
    }

def get_book(book_id):
    # print(books[book_id])
    print(f"\n\nBook Detail :--\n{book_id} | {books[book_id]['Title']} by {books[book_id]['Author']} ({books[book_id]['Year']}) - Copies: {books[book_id]['copies']}\n\n")

while 1:
    print("1. Add new Book\n2. Display book by Book_id\n3. Exit")
    c = int(input('Enter Your Choice:--'))

    match c:
        case 1:
            print("Enter Book Details ID , Title , Author , Year , Copies")
            id = input()
            title = input()
            author = input()
            year = int(input())
            copies = input()
            add_book(id , title , author , year , copies)

        case 2:
            id = input("Enter Book ID:--")
            get_book(id)

        case 3:
            print("Exit")

            break




# class Book :
#     def __init__(self , book_id , title , author , year , copies):
#         self._book_id = book_id
#         self._title = title
#         self._author = author
#         self._year = year
#         self._copies = copies
#
#     def isAvailable(self):
#         return self._copies > 0
#
#     def availableCopies(self):
#         return self._copies
#
#
# class Members:
#     def __init__(self , member_id , name , number):
#         self._member_id = member_id
#         self._name = name
#         self._number = number
#
#     def getMemberDetails(self):
#         return {
#             'id' : self._member_id,
#             'name' : self._name,
#             'number' : self._3
#         }
#
#
# class Staff:
#     def __init__(self , staff_id , name , role):
#         self._staff_id = staff_id
#         self._name = name
#         self._role = role
#
#     def getStaffDetails(self):
#         return {
#             'id' : self._staff_id,
#             'name' : self._name,
#             'role' : self._role
#         }
#
# class Library:
#     def __init__(self):
#         self.books = {}
#
#     def add_book(self):
