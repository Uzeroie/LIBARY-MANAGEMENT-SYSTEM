import Date
import ShowBooks

def Return_Book():
    name=input("Enter name of the borrower: ")
    borrow_book="Book borrowed by "+name+".txt"
    #Checking if borrower name matches existing borrower file
    try:
        with open(borrow_book,"r") as file:
            line=file.readlines()
            line=[borrow_book.strip("$") for return_book in line]

        with open(borrow_book,"r") as file:
            line2=file.read()
    except:
        print("\nThe name of borrower doesn't exist.")
        Return_Book()

    #Creating a text file for returned book
    return_book="Book returned by "+name+".txt"
    with open(return_book,"w+") as file:
        file.write("----------------------------------------------------------\n\t\tReturn Details Details:\n-------------------------------------------------------------\n")
        file.write("\t\tBook Returned by: "+name+"\n")
        file.write("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
        file.write("\n----------------------------------------------------------------------------------------------------------------------\n\t\t Bookname\t\t Author name\t\t Price($)\n----------------------------------------------------------------------------------------------------------------------")

    Total_Cost=0.0
    for i in range(5):
        if ShowBooks.Book_Name[i] in line2:
            with open(return_book,"a") as file:
                file.write("\n\t\t"+ShowBooks.Book_Name[i]+"\t\t"+ShowBooks.Author_Name[i]+"\t\t"+ShowBooks.Price[i]+"\n")
                ShowBooks.Quantity[i]=int(ShowBooks.Quantity[i])+1
            Total_Cost += float(ShowBooks.Price[i])
    print("----------------------------------------------------------\n\t\tReturn Details Details:\n-------------------------------------------------------------\n")
    print("\t\tBook Returned by: "+name+"\n")
    print("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
    print("\n---------------------------------------------------------------------------------------------\n\t\t Bookname\t\t Author name\t\t Price($)\n----------------------------------------------------------------------------------------------------")
    print("\n\t\t"+ShowBooks.Book_Name[i]+"\t\t"+ShowBooks.Author_Name[i]+"\t\t"+ShowBooks.Price[i]+"\n")
    #if day is exceeded  total comes with fine
    exceed=int(input("Enter total days of books being borrowed: "))
    if exceed>7:
        print(Total_Cost)
        days=exceed-7
        fine= 5*days
        Total_Cost+=fine
        with open(return_book,"a") as file:
            file.write("\n Your fine for late submission of book is: $"+str(fine)+"\n")
            file.write("\n Your Total Fine is: $"+str(Total_Cost)+"\n")
        print("----------------------------------------------------------\n\t\tReturn Details Details:\n-------------------------------------------------------------\n")
        print("\t\tBook Returned by: "+name+"\n")
        print("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
        print("\n----------------------------------------------------------------------------------------------------------------------\n\t\t Bookname\t\t Author name\t\t Price($)\n----------------------------------------------------------------------------------------------------------------------")
        print("\n\t\t"+ShowBooks.Book_Name[i]+"\t\t"+ShowBooks.Author_Name[i]+"\t\t"+ShowBooks.Price[i]+"\n")
        print("\nYour fine is: $"+str(fine)+"\n")
        print("\nYour TotalCost is: $"+str(Total_Cost)+"\n")
        
    else:
        print("----------------------------------------------------------\n\t\tReturn Details Details:\n-------------------------------------------------------------\n")
        print("\t\tBook Returned by: "+name+"\n")
        print("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
        print("\n----------------------------------------------------------------------------------------------------------------------\n\t\t Bookname\t\t Author name\t\t Price($)\n----------------------------------------------------------------------------------------------------------------------")
        print("\n\t\t"+ShowBooks.Book_Name[i]+"\t\t"+ShowBooks.Author_Name[i]+"\t\t"+ShowBooks.Price[i]+"\n")
    with open("books.txt","w+") as file:
        for i in range(5):
            file.write(ShowBooks.Book_Name[i]+","+ShowBooks.Author_Name[i]+","+str(ShowBooks.Quantity[i])+","+ShowBooks.Price[i]+"\n")   
