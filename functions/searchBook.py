#search book by book name
def search_book(book_name , books):
    #1. create empty book dict
    book = {}

    #2. loop over the books dict and get append all the book that match the book name given by user
    for book_id in books:
        #convert book title to lower case to find book easily
        lower_title = books[book_id]['Title'].lower()
        if(lower_title.count(book_name)):
            book[book_id] = books[book_id]



    if len(book) > 0:
        print("\nBook_ID\n")
        for book_id in book:
            print(f"{str(book_id).ljust(6 , ' ')} | {books[book_id]['Title']} by {books[book_id]['Author']} ({books[book_id]['Year']}) - Copies: {books[book_id]['copies']}\n")
    else:
        print("\nBook is not found\n")

    return book