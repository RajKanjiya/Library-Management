from functions.searchBook import search_book

def update_book(book_name , books):
    book = search_book(book_name , books)

    if len(book) == 0:
        return

    book_id = input("Enter book id that you want to update :-- ")

    print(
        f"\n{book_id} | {books[book_id]['Title']} by {books[book_id]['Author']} ({books[book_id]['Year']}) - Copies: {books[book_id]['copies']}\n")

    print(
        "1. Edit Title\n2. Edit Author Name\n3. Edit Year\n4. Edit Copies\n5. Nothing to Edit")
    c = int(input('Enter Your Choice:--'))

    match c:
        case 1:
            title = input("Enter Title :--")
            books[book_id]['Title'] = title
        case 2:
            auth_name = input("Enter Auther Name :-- ")
            books[book_id]['Author'] = auth_name
        case 3:
            year = input("Enter Year :-- ")
            books[book_id]['Year'] = year
        case 4:
            copies = input("Enter Copies :-- ")
            books[book_id]['copies'] = copies
        case 5:
            print("Exit")
            return