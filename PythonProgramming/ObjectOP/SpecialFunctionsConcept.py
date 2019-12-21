class Book():
    pass

book = Book() ## __init__ is called

print(book)  ## __str__ function is called

"""
# it is used to delete object
del book
book

"""

class Book():

    def __init__(self, name, writer, numOfPage, kindBook):

        print("init function")
        self.name = name
        self.writer = writer
        self.numOfPage = numOfPage
        self.kindBook = kindBook

    def __str__(self):
        return "Name: {}\nWriter: {}\nNumber of Page: {}\nBook Kind: {}\n".format(self.name,
                                                                                  self.writer,
                                                                                  self.numOfPage,
                                                                                  self.kindBook)
    def __len__(self):
        return self.numOfPage

book = Book("Java Learning", "Robert Bro", 560, "Programming")
print(book)
print(len(book))


