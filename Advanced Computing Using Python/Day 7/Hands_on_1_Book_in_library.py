
# class Book:
#     def __init__(self, title, author, year, available = True):
#         self._title = title
#         self._author = author
#         self._year = year
#         self._available = available
#
#     def display_details(self):
#         print(f"\nBook Title: {self._title}\nBook Author: {self._author}\nBook Year: {self._year}\nAvailability: {'Available' if self._available else 'Not available'}")
#
#     def borrow_book(self):
#         if not self._available:
#             print(f"\nThe book {self._title} is Not Available.")
#             return
#         self._available = False
#         print(f"\n{self._title} book has been Borrowed.")
#
#     def return_book(self):
#         self._available = True
#         print(f"\n{self._title} book has been Returned.")
#
# if __name__ == '__main__':
#     # Creating two books
#     book1 = Book(
#         title = 'title1',
#         author = 'author1',
#         year = '1234',
#     )
#     book2 = Book(
#         title = 'title2',
#         author = 'author2',
#         year = '2345'
#     )
#
#     # Displaying their information
#     book1.display_details()
#     book2.display_details()
#
#     # borrowing one book and checking status
#     book1.borrow_book()
#     book1.display_details()
#
#     # returning book
#     book1.return_book()
#     book1.display_details()

# ___________________________________________________________________________

class Book:
    # title = ""
    # author = ""
    # year = None
    # available = True
    books_available = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.__year = year
        self.available = True

    def set_year(self,year):
        self.__year = year

    def get_year(self):
        return self.__year

    def borrow_book(self):
        if self.available == True:
            self.available = False
            print(f"{self.title} has been borrowed")
        else:
            print(f"{self.title} is not available")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned")


    def display_details(self):
        print(f"Book Title: {self.title} Book Author: {self.author} Book Year of Publication: {self.__year} Availability: {self.available}")

    @staticmethod
    def message():
        print("Books are mans best friend!")

    @classmethod
    def example_classMethod(cls):
        cls.books_available += 1
        print(f"Books available : {cls.books_available}")
        print("Books are mans best friend!!")


book1 = Book("Atomic Habbits", "Dont Know", 2016)
book2 = Book("Laws of human nature", "Robert", 2020)

book1.display_details()
book2. display_details()

book1.borrow_book()
book1.borrow_book()
book2.return_book()

book1.example_classMethod()
Book.message()
book2.example_classMethod()

book1.set_year(5000)
book1.__year=10000

print(f"Book Name : {book1.title} Book year: {book1.get_year()}")
