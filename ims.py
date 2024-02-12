class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if books:
            print("List of Books:")
            for book in books:
                title, author, _, _ = book.split(',')
                print(f"Book: {title}, Author: {author}")
        else:
            print("No books available.")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter book title to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        self.file.seek(0)
        updated_books = [book for book in books if title not in book]
        self.file.truncate(0)
        self.file.writelines(updated_books)
        print("Book removed successfully.")


lib = Library()
while True:
    print("\n*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")