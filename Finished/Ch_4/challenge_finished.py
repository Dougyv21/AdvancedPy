# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for Special Class Methods
from enum import Enum

# Challenge:
# Given a class that represents a Book with various properties such
# as title, author, pagecount, etc:
# 1) Implement the __repr__ and __str__ functions to output:
#   str:  "(title) by (author): (pagecount), (cover), (price)"
#   repr: "<Book:title:author:pages:cover:antique:genre:price>"
# 2) Implement the comparison methods to allow comparing books based
#   on pagecount.
# 3) Implement an enum that represents the type of the book cover. The
#   allowable cover types are "hard" and "paperback". Replace the existing
#   "Hard" and "paperback" strings with the enum.
# 4) Implement an "adjustedprice" computed attribute - books that are antiques
#   have a 10.00 surcharge on their price, Paperback books get a 2.00 discount
# 5) Successfully execute the sample code provided below.


class Book():
    def __init__(self, title, author, pages, cover, antique, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover = cover
        self.antique = antique
        self.price = price

    # TODO: Implement the str and repr functions
    def __str__(self) -> str:
        return f"{self.title} by {self.author}: {self.pages}, {self.cover}, {self.price}"

    def __repr__(self) -> str:
        return f"<Book:{self.title}:{self.author}:{self.pages}:{self.cover}:{self.antique}:{self.price}>"

    # TODO: Implement the adjustedprice attribute
    def __getattr__(self, attr):
        if attr == "adjustedprice":
            val = self.price
            if self.antique == True:
                val += 10.0
            if self.cover == CoverType.PAPERBACK:
                val -= 2.0
            return val

    # TODO: Implement comparisons <, >, <=, >=
    def __ge__(self, other):
        return self.pages >= other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __lt__(self, other):
        return self.pages < other.pages


# TODO: Implement the Hard/Paperback Enum
class CoverType(Enum):
    HARD = 0
    PAPERBACK = 1


books = [
    Book("War and Peace", "Leo Tolstoy", 1225,
         CoverType.HARD, True, 29.95),
    Book("Brave New World", "Aldous Huxley",
         311, CoverType.PAPERBACK, True, 32.50),
    Book("Crime and Punishment", "Fyodor Dostoevsky",
         492, CoverType.HARD, False, 19.75),
    Book("Moby Dick", "Herman Melville", 427,
         CoverType.PAPERBACK, True, 22.95),
    Book("A Christmas Carol", "Charles Dickens",
         66, CoverType.HARD, False, 31.95),
    Book("Animal Farm", "George Orwell", 130,
         CoverType.PAPERBACK, False, 26.95),
    Book("Farenheit 451", "Ray Bradbury", 256,
         CoverType.HARD, True, 28.95),
    Book("Jane Eyre", "Charlotte Bronte", 536,
         CoverType.PAPERBACK, False, 34.95)
]

# TEST CODE

# 1 - test the str and repr functions
print("-------------")
print(str(books[0]))
print(str(books[3]))
print(str(books[5]))
print()
print(repr(books[0]))
print(repr(books[3]))
print(repr(books[5]))
print("-------------")
print()

# 2 - test the "adjustedprice" computed attribute
for book in books:
    print(f"{book.title}: {book.adjustedprice:.2f}")
print("-------------")
print()

# 3 - compare on pagecount
print(books[1] > books[2])
print(books[4] < books[6])
print(books[7] >= books[0])
print(books[3] <= books[4])
