#add book
def add_book(book_id , title , author , year , copies , books):
    if(book_id in books):
        print(f"This book ID is already exist")
        return

    books[book_id] = {
        'Title' : title,
        'Author' : author,
        'Year' : year,
        'Copies' : copies
    }

    print("Book successfully added")