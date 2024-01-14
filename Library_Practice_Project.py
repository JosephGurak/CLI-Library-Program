class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
#HELLO!!!!!

class Book:
    def __init__(self, title, author, year_published, genre, age_category):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.genre = genre
        self.age_category = age_category

    def __str__(self):
        return f"{self.title} \033[1;35mBy:\033[0;0m {self.author} \033[1;35mPublished:\033[0;0m{self.year_published} \033[1;35mGenre:\033[0;0m {self.genre} \033[1;35mAge Category:\033[0;0m {self.age_category}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f"Book '{book.title}' added to the library.")
        else:
            print(f"Book '{book.title}' is already in the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)


class Member:
    def __init__(self, name, library, age):
        self.name = name
        self.library = library
        self.age = age

    def borrow_book(self, book_title):
        available_books = [book for book in self.library.books if book.title.lower() == book_title.lower()]
        if available_books:
            book = available_books[0]
            if book.age_category == 'Adult' and self.age < 18:
                print(f"'{book.title}' is an adult book. You must be 18 or older to borrow it.")
            else:
                print(f"{self.name} borrowed '{book.title}' from the library.")
                self.library.books.remove(book)
        else:
            print(f"\033[31;1;4m'{book_title}' is not available in the library. \033[0m")


def create_account():
    print('\n\t\033[4;34m Create your MathSharp Library Account \033[0;0m\n')
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    age = int(input("Enter your age: "))
    return User(username, password, age)


def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in users:
        if user.username == username and user.password == password:
            return user

    print("\033[31;1;4m Invalid username or password \033[0m")
    return None

users = []
library = Library()

while True:
    print("\n\t\033[4;34m Welcome to the MathSharp Library for Digital Resources \033[0;0m\n")
    print("\nPlease Create an account, then log in to access the Other Options on the List")
    print("1. Create an account")
    print("2. Log in")
    print("3. Display available books")
    print("4. Add a book to the library")
    print("5. Borrow a book")
    print("6. Exit")

    choice = input("Choose an Option: ")

    if choice == "1":
        new_user = create_account()
        users.append(new_user)
        print("Account created successfully.")
    elif choice == "2":
        logged_in_user = login(users)
        if logged_in_user:
            member = Member(logged_in_user.username, library, logged_in_user.age)
            print(f"Welcome, {logged_in_user.username}!")
    elif choice == "3":
        library.display_books()
    elif choice == "4" and logged_in_user is not None:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        year_published = input("Enter the year of publication: ")
        genre = input("Enter the genre of the book: ")
        age_category = input("Enter the age category of the book (Children/Adult): ")

        new_book = Book(title, author, year_published, genre, age_category)
        library.add_book(new_book)
    elif choice == "5" and logged_in_user is not None:
        book_title = input("Enter the title of the book you want to borrow: ")
        member.borrow_book(book_title)
    elif choice == "6":
        print("Exiting the Mathsharp library program. Auf Wiedersehn!")
        break
    else:
        print("\033[31;1;4m Please enter a valid option.\033[0m")
