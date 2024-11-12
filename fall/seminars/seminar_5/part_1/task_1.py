class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        if self.pages > 300:
            return True
        else:
            return False

    def short_description(self):
        return f"{self.title} by {self.author}"


my_book = Book("A Byte of Python", "Swaroop C.H.", 123)

print(my_book.is_long())
print(my_book.short_description())