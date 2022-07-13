def ShowBooks():
    global Book_Name
    global Author_Name
    global Quantity
    global Price
    ##Creating empty list to append .txt file values
    
    Book_Name=[]
    Author_Name=[]
    Quantity=[]
    Price=[]

    with open("books.txt","r") as file:
        read_lines=file.readlines()
        read_lines=[each.strip("\n") for each in read_lines]
        for i in range(len(read_lines)):
            count=1
            for j in read_lines[i].split(","):
                if(count==1):
                    Book_Name.append(j)
                    
                elif(count==2):
                    Author_Name.append(j)
                    
                elif(count==3):
                    Quantity.append(j)
                     
                elif(count==4):
                    Price.append(j.strip("$"))
                count+=1
