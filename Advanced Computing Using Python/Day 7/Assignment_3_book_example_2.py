
class Book:
    no_of_copies = 1

    def __init__(self, title, author, year, available = True):
        self._title = title
        self._author = author
        self.__year = year
        self._available = available

    def print_year(self):
        print(self.__year)

    @classmethod
    def add_copies(cls, additional_copies):
        Book.no_of_copies += additional_copies

    @staticmethod
    def static_example():
        print("Books are man's best friend.")

    def display_details(self):
        print(f"\nBook Title: {self._title}\nBook Author: {self._author}\nBook Year: {self._year}\nCopies: {self.no_of_copies}\nAvailability: {'Available' if self._available else 'Not available'}")

    def borrow_book(self):
        if not self._available:
            print(f"\nThe book {self._title} is Not Available.")
            return
        self._available = False
        print(f"\n{self._title} book has been Borrowed.")

    def return_book(self):
        self._available = True
        print(f"\n{self._title} book has been Returned.")

if __name__ == "__main__":
    book1 = Book(
        title = 'title1',
        author = 'author1',
        year = '2134'
    )
    book2 = Book(
        title = "title2",
        author = 'author2',
        year = '1234'
    )
    # book1.add_copies(2)
    # print(book1.no_of_copies)
    # print(book2.no_of_copies)
    # book1.static_example()
    # Book.static_example()
    book1.print_year()
    print(book1.__year)

    pass