#get book details by book id
def get_book(book_id , books):
    print(f"\n\nBook Detail :--\n{book_id} | {books[book_id]['Title']} by {books[book_id]['Author']} ({books[book_id]['Year']}) - Copies: {books[book_id]['copies']}\n")

#get all book
def get_all_books(books):
    print("\n\nAll Books Detail :--\n")
    for book_id in books:
        print(f"{book_id} | {books[book_id]['Title']} by {books[book_id]['Author']} ({books[book_id]['Year']}) - Copies: {books[book_id]['copies']}\n")
    print()