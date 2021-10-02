n=5 # total no of books of each quantity
class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict =  {}
        
    def displayBook(self):
        print(f"We have followings books in our library: {self.name} ")

        print('{\'Name of book\' : quantity} ->', self.bookslist)

    def lendBook(self, user, book,n):
        if book not in self.bookslist.keys():
            print('sorry',book,'book is not avaliable')
        else:
            if book not in self.lendDict.keys():
                self.lendDict.update({user : [book]})
                print("Lender-book database has been updated. You can take the book now")
                self.bookslist.update({book:n})
            else:
                print(f"Book is already being used by {self.lendDict[book]}")


    def addBook(self, book,n):
        if book in self.bookslist.keys():
            self.bookslist.update({book:n})
            print("book has been added to the book list")

        else:
            q=int(input('enter quantity of book : '))
            self.bookslist.update({book:q})
    def returnBook(self,book,n):
        self.bookslist.update({book:n})
        print("book has been returned sucessfully")

if __name__ == '__main__':

    harry = Library({'python': n,'rich dad poor dad':n,'harry potter':n,'c++ basics':n,'algorithms by clrs': n}, "Code with shubham")

    while True:
        print("Welcome to the {harry.name} library. Enter your choice to continue")
        print('1. Display Books')
        print('2. Lend a Book')
        print('3. Add a Book')
        print('4. Return a Book')
        
        user_choice =int(input())
        
        if user_choice ==1:
            harry.displayBook()
            
        elif user_choice ==2:

            book = input("Enter the name of the book you want to lend: ")
            book = book.lower()
            user = input("Enter your name : ")
            user=user.lower()
            harry.lendBook(user, book,n-1)
            '''print("to lend another book respond with y/n")
            user_choice3 = ""
            while (user_choice3 != "y" and user_choice3 != "n"):
                user_choice3 = input()
            if user_choice3 == "n":
                continue
            if user_choice3 == "y":
                book = input("Enter the name of the book you want to lend: ")
                user=user
                book = book.lower()
                harry.lendBook(user, book, n - 1)'''
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            harry.addBook(book,n+1)
            
            
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            harry.returnBook(book,n+1)
            
            
        else:
            print("Not a valid option")
            
        print("Press q to quit and c to continue")
        user_choice2 =""
        while (user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
        if user_choice2 == "q":
            exit()
            
        if user_choice2 == "c":
            continue

    print(type(self.bookslist))
        
            
            
        
