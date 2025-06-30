class Library:
    books = []  # Class variable to store all book objects

    def __init__(self, bookname, author):
        self.bookname = bookname
        self.author = author

    def display(self):
        print(f"Book Name: {self.bookname}, Author: {self.author}")

    @classmethod
    def add_new_book(cls):
        bookname = input("Enter the book name: ")
        author = input("Enter the author's name: ")
        book = Library(bookname, author)
        cls.books.append(book)
        print("Book added successfully.\n")

    @classmethod
    def view_books(cls):
        if not cls.books:
            print("No books added yet.\n")
            return
        for book in cls.books:
            book.display()

    @classmethod
    def search_books(cls):
        search_bookname = input("Enter book name to search: ")
        found = False
        for book in cls.books:
            if book.bookname.lower() == search_bookname.lower():
                book.display()
                found = True
        if not found:
            print("Book not found.\n")


# Menu-driven program
while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book by Name")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        Library.add_new_book()
    elif choice == '2':
        Library.view_books()
    elif choice == '3':
        Library.search_books()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
