import Date
import ShowBooks
import borrow_Book
import return_book

def main():
    loopExit=0
    while loopExit==0:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
        print("                     Library Management System                          ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        with open("books.txt","r") as file:
            file= open("books.txt","r")
            Dict={}
            BookID=1
        for line in file:
            a=line.replace("\n"," ")
            b=a.split(",")
            Dict.update({str(BookID):b})
            BookID=BookID+1
        print("--------------------------------------------------------------------------------")
        print("{:<11} {:<26} {:<20} {:<10} {:<10} ".format('Book ID','Book Name','Author Name','Quantity','Price'))
        print("--------------------------------------------------------------------------------")

        for key,value in (Dict.items()):
            bookname, authorname, quantity, price =value
            Tabular_Value=("{:<11}{:<26} {:<22} {:<10} {:<10}".format(key,bookname, authorname, quantity, price))
            print(Tabular_Value)
        print("--------------------------------------------------------------------------------")
            
        print("Enter '1' To Borrow a book")
        print("Enter '2' To Return a book")
        print("Enter '3' To Exit")
        num=input("\nEnter a number:")

        try:
            if num=="1":
                ShowBooks.ShowBooks()
                borrow_Book.borrow_book()
            elif num=="2":
                ShowBooks.ShowBooks()
                return_book.Return_Book()
            elif num=="3":
                print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""\n \t \t \t Thank you for using library management system","\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                loopExit=loopExit+1
            else:
                print("Invalid input!! Please enter a choice from 1-3")
        except ValueError:
            print("Please input values as suggested above.")
main()
