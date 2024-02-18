#Lib class
class Library:
    def __init__(self,file_name='book.txt'):
        self.file_name = file_name
        self.file = open(self.file_name,"a+",encoding="utf-8")

        #Starting the program
        self.start_lib()

    def start_lib(self):
        self.menu()

        while True:
            selection = input("Please select the action : ")

            if selection == "1":
                self.list_books()
                print("*****************************************************************************************************")
                self.menu()
            elif selection == "2":
                book_name = input("Enter name of the book : ")
                autor = input("Enter autor of the book : ")
                publish_date = input("Enter publish date of the book : ")
                total_pages = input("Enter total pages of the book : ")
                self.add_book(book_name,autor,publish_date,total_pages)
                print("*****************************************************************************************************")
                self.menu()
            elif selection == "3":
                book_name = input("Please enter name of the book that you want to remove from system :")
                self.remove_book(book_name)
                print("*****************************************************************************************************")
                self.menu()
            elif selection == "q" or selection == "Q":
                print("Exiting the system...")
                break
            else:
                print("Invalid action.")

    #Menu
    def menu(self):
        print("-----------------------------------------------------------------------------------------------------")
        print("|                                  Library Management System                                        |")
        print("-----------------------------------------------------------------------------------------------------")
        print("*** MENU ***")
        print("""1) List Books\n2) Add Book\n3) Remove Book\nPress 'q' to exit""")

    #Listing books
    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()

        #Table Headers
        print("{:<5} {:<30} {:<30} {:<15} {:<10}\n".format("No","Book Title","Autor","Publish Date","Total Pages"))

        for index, book in enumerate(iterable=books,start=1):
            book_info = book.split(" ,")
            book_name = book_info[0]
            autor = book_info[1]
            publish_date = book_info[2]
            total_pages = book_info[3]

            #Display
            print("{:<5} {:<30} {:<30} {:<15} {:<10}".format(index,book_name,autor,publish_date,total_pages))


    #Adding book
    def add_book(self,book_name,autor,publish_date,total_pages):

        #Capitialize first letters before saving 
        book_name = book_name.title()
        autor = autor.title()

        #Calling is_duplicated method
        if self.is_duplicated(book_name,autor):
            print(f"Error! {book_name} is already in the system. You can\'t add same book twice!")
            return

        #Checking if the publish date and total pages contain numbers only
        if not(str(publish_date).isdigit() and str(total_pages).isdigit()):
            print("Error! Publish date and total pages must be in numbers")
            return

        self.file.write("{book_name} ,{autor} ,{publish_date} ,{total_pages}".format(book_name=book_name,autor=autor,publish_date=publish_date,total_pages=total_pages)+"\n")
        print(f"{book_name} is successfully added to system!")
    
    #Removing a book 
    def remove_book(self,book_name):
        book_to_delete = book_name.title()
   
        #Reading all the lines in text file before rearranging it
        with open(self.file_name,"r",encoding="utf-8") as file:
            lines = file.readlines()
        
        #Creating a condition to rewrite the document without the book desired to be deleted
        with open(self.file_name,"w",encoding="utf-8") as file:
            is_removed = False
            for line in lines:
                if f"{book_to_delete}" not in line :
                    file.write(line)
                else:
                    confirm = input("Are you sure to proceed? Y/n : ")
                    if confirm == "Y":
                        print(f"{book_to_delete} is removed from the system.")
                        is_removed = True
                    elif confirm == "n":
                        print("The operation is cancelled.")
                        file.writelines(lines)
                        return
                    else:
                        print("Invalid action.")
                        file.writelines(lines)
                        return
            if not is_removed:
                print(f"{book_to_delete} is not found in the system.")

    #Preventing duplicate records
    def is_duplicated(self,book_name,autor):
        with open(self.file_name,"r",encoding="utf-8") as file:
            for book in file:
                if f"{book_name} ,{autor}" in book:
                    return True
        return False

    def __del__(self):
        self.file.close()

my_file = Library()
