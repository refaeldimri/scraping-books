from app import books

USER_CHOICE = '''\n Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''

book_generator = (x for x in books)


def print_best_book():
    best_book = list()
    for book in books:
        if book.rating == 5:
            best_book.append(book)
    for book in best_book:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheapest_books:
        print(book)


def get_next_book():
    print(next(book_generator))


def menu():
    user_input = None
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n'):
            userChoice[user_input]()
            user_input = input(USER_CHOICE)
        else:
            print("try again")
            user_input = input(USER_CHOICE)


userChoice = {
    'b': print_best_book,
    'c': print_cheapest_books,
    'n': get_next_book
}


menu()



