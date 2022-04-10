class Library:
    def __init__(self, ListOfBooks):
        self.books = ListOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in this Library are: ")
        for book in self.books:
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days.")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued by someone else. Please wait until the book is available")
            return False


    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")

class Student:

    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django", "clrs", "Python Notes"]) 
    student = Student()
    centralLibrary.displayAvailableBooks()


while(True):
    welcomeMsg = '''\n ***** WELCOME TO CENTRAL LIBRARY *****
    Please choose an option:
    1. List of Books.
    2. Request a Book.
    3. Add/Return a Book.
    4. Exit the Library.
    '''
    print(welcomeMsg)

    a = int(input("Enter an option: "))
    if a==1:
        centralLibrary.displayAvailableBooks()   
    elif a==2:
        centralLibrary.borrowBook(student.requestBook())
    elif a==3:
        centralLibrary.returnBook(student.returnBook())
    elif a==4:
        print("Thanks for choosing central Library. Have a greet day ahead!")
        exit()
    else:
        print("Invalid choice!")

