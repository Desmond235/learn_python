
class Book:
    def __init__(self,title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.title

    def __lt__(self, other):
        return self.num_pages == other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

book1 = Book('Hobbit', 'J.R.R. Tolkein', 310)
book2 = Book("Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 223)
book3 = Book("The Lion, the Witch and the Wardrobe", 'C.S Lewis', 172)

print(book1)
print(book1 > book2)