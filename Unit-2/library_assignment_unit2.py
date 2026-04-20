class Library:

    def __init__(self, book_name, author, status):
        self.book_name = book_name
        self.author = author
        self.status = status

    def check_out(self):
        if self.status == "available":
            self.status = "not available"
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        self.status = "available"
        print("Book returned")

    def display(self):
        if self.status == "available":
            print(self.book_name, "-", self.author)


b1 = Library("Python", "Guido", "available")

b1.display()
b1.check_out()
b1.return_book()
b1.display()