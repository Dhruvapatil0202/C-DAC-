from tabulate import tabulate

CHOICE_STR = """
1. Display all Books
2. Search Book 
3. Add Book
4. Remove Book
5. Exit
Enter Your Choice: """


def print_tabulation(data, header):
    tabulation = tabulate(data, header, tablefmt= 'grid')
    print(tabulation)

def display_books(book_record_dict):

    if not book_record_dict:
        print("\nThe Collection Does not have any book! ")
        return

    header = ['Title', 'Author', 'Genre', 'Publication Year']
    data = [[book, book_record_dict[book]['author'], book_record_dict[book]['genre'], book_record_dict[book]['publication_year']] for book in book_record_dict]
    print_tabulation(data, header)
    print('\n')

def add_book(book_record_dict):

    title = input("Enter title of book: ")
    author = input(f"Enter author of {title}: ")
    genre = input(f"Enter genre of {title}: ")
    publication_year =  input(f"Enter Publication year of {title}: ")

    if title in book_record_dict and (author == book_record_dict[title]['author'] and
                                      genre == book_record_dict[title]['genre'] and
                                      publication_year == book_record_dict['publication_year']):
        print("Book Already Present in Book collection: ")
        return book_record_dict

    book_record_dict[title] = {'author': author,
                               'genre': genre,
                               'publication_year': publication_year}

    return book_record_dict

def remove_book(book_record_dict):

    title = input("Enter title of book you want to remove: ")
    if title not in book_record_dict:
        print(f"\n{title} does not exist in book collection. ")
        return book_record_dict

    del book_record_dict[title]

    return book_record_dict

def search_book(book_record_dict):

    choice = "x"
    while choice not in '12':
        choice = input("Search books by: 1. Author or 2. Genre: ")
        if choice not in "12": print("Invalid input! ")

    match choice:
        case "1":
            cand_author = input("\nEnter name of author to search the book: ")
            data = []
            for book in book_record_dict:
                if book_record_dict[book]['author'] == cand_author:
                    data.append([book, cand_author, book_record_dict[book]['genre'], book_record_dict[book]['publication_year']])
            if not data:
                print(f"Books of {cand_author} does not exist in book collection. ")
            else:
                header = ['Title', 'Author', 'Genre', 'Publication Year']
                print_tabulation(data, header)

        case "2":
            cand_genre = input("\nEnter name of Genre to search the book: ")
            data = []
            for book in book_record_dict:
                if book_record_dict[book]['genre'] == cand_genre:
                    data.append([book, book_record_dict[book]['author'], cand_genre, book_record_dict[book]['publication_year']])
            if not data:
                print(f"Books of {cand_genre} genre does not exist in book collection. ")
            else:
                header = ['Title', 'Author', 'Genre', 'Publication Year']
                print_tabulation(data, header)

if __name__ == '__main__':

    book_records = {}
    while True:

        resp = input(CHOICE_STR)
        match resp:
            case "1":
                display_books(book_records)
            case "2":
                search_book(book_records)
            case "3":
                book_records = add_book(book_records)
            case "4":
                book_records = remove_book(book_records)
            case "5":
                break
            case _:
                print("\n Invalid Input!!\n")

