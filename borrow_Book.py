import Date
import ShowBooks

def borrow_book():
    borrow= False 
    while True:
        name=input("Please Enter your name: ")
        if name.isalpha(): ##Checks wether the user giver value is alphabet or not.
            break
        print('Please enter your name \nExample: IraLamichhane')
    borrow_note="Book borrowed by "+name+".txt" ##Creating Text file with user's given name
    
    with open(borrow_note,"w+") as file:
        file.write("----------------------------------------------------------\n\t\tBorrow Details:\n-------------------------------------------------------------\n")
        file.write("\t\tBook borrowed by: "+name+"\n")
        file.write("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
        file.write("\n--------------------------------------------------------------------------------------------\n\t\t Bookname\t\t Author name\t\t Price\n----------------------------------------------------------------------------------------------------------------------")
      
    while borrow== False:
        print("\nPlease select a book to borrow.\n")
        for i in range(len(ShowBooks.Book_Name)):
            print("Enter",i,"to borow",ShowBooks.Book_Name[i])
        try:
            borrowing_book=int(input("\nPlease select from above option to borrow book: "))
            try:
                if(int(ShowBooks.Quantity[borrowing_book])>0):
                    print("\n-----------------------\n The Book is available\n.-----------------------")
                    with open(borrow_note,"a") as file:
                        file.write("\n\t\t"+ShowBooks.Book_Name[borrowing_book]+"\t\t"+ShowBooks.Author_Name[borrowing_book]+"\t\t"+ShowBooks.Price[borrowing_book]+"\n")
                    

                    #Updating Quantity
                    ShowBooks.Quantity[borrowing_book]=int(ShowBooks.Quantity[borrowing_book])-1
                    with open("books.txt","w+") as file:
                        for i in range(5):
                            file.write(ShowBooks.Book_Name[i]+","+ShowBooks.Author_Name[i]+","+str(ShowBooks.Quantity[i])+","+ShowBooks.Price[i]+"\n")
                    print("----------------------------------------------------------\n\t\tBorrow Details:\n-------------------------------------------------------------\n")
                    print("\t\tBook borrowed by: "+name+"\n")
                    print("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
                    print("\n-------------------------------------------------------------------------------------\n\t\t Bookname\t\t Author name\t\t Price($)\n---------------------------------------------------------------------------------")
                    print("\n\t\t"+ShowBooks.Book_Name[borrowing_book]+"\t\t"+ShowBooks.Author_Name[borrowing_book]+"\t\t"+ShowBooks.Price[borrowing_book]+"\n")
                    #Borrowing multiple books
                    x=1
                    while x==1:
                        more_Books=input("Enter y to borrow more books OR n to end: ").lower()
                        if more_Books=="y":
                            print("Please Select to borrow book.\n")
                            for i in range(len(ShowBooks.Book_Name)):
                                print("Enter",i,"to borow",ShowBooks.Book_Name[i])
                                
                            borrowing_book=int(input("Please select above option to borrow book: "))
                            
                            if(int(ShowBooks.Quantity[borrowing_book])>0):
                                print("-----------------------\n The book is available\n.-----------------------")
                                with open(borrow_note,"a") as file:
                                    file.write("\n\t\t"+ShowBooks.Book_Name[borrowing_book]+"                  "+ShowBooks.Author_Name[borrowing_book]+"                        "+ShowBooks.Price[borrowing_book]+"\n")

                                

                                #Updating Quantity
                                ShowBooks.Quantity[borrowing_book]=int(ShowBooks.Quantity[borrowing_book])-1
                                with open("books.txt","w+") as file:
                                    for i in range(5):
                                        file.write(ShowBooks.Book_Name[i]+","+ShowBooks.Author_Name[i]+","+str(ShowBooks.Quantity[i])+","+ShowBooks.Price[i]+"\n")
                                print("----------------------------------------------------------\n\t\tBorrow Details:\n-------------------------------------------------------------\n")
                                print("\t\tBook borrowed by: "+name+"\n")
                                print("\t\tDate :"+Date.date()+" Time: "+Date.time()+"\n")
                                print("\n----------------------------------------------------------------------------------------------------------------------\n\t\t Book Name\t\t Author Name\t\t Price\n----------------------------------------------------------------------------------------------------------------------")
                                print("\n\t\t"+ShowBooks.Book_Name[borrowing_book]+"\t\t"+ShowBooks.Author_Name[borrowing_book]+"\t\t"+ShowBooks.Price[borrowing_book]+"\n")
                            else:
                                print("Sorry, The book is not availabel")
                                
                        elif(more_Books=="n"):
                            print("-----------------------------\n \t\t\tThank you for borrowing a book.\n-----------------------------")
                            borrow=True
                            x+=1
                            break
                            print("Invalid Input!! Please input values as instructed")
                    

                else:
                    print("-----------------------\nSorry, The choosen Book is not available\n.-----------------------")
                    
                        
            except IndexError:
                print("\nPlease choose a book from above number.")
        except ValueError:
            print("\nError input!!!")



