
# create_user()

from components import *
from fileop import *
from project_functions import *
from users_functions import *


# Main 

while True:
    print("---------------------------Saving Private Fund----------------------------")
    print("1. Create accout")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice number: ")
    if choice == "1":
        create_user()
    elif choice == "2":
        name, index, exist = login()
        while True:
            if exist:
                print("--------------------------------------------------------")
                print(f"Welcome {name} you can choose from the following: ")
                print("--------------------------------------------------------")
                print("1. Create Project")
                print("2. View Projects")
                print("3. Delete Project")
                print("4. Edit Project")
                print("5. Search") 
                print("6. Log out") 
                choice = input("Enter choice number: ")
                if choice == "1":
                    create_project(index)
                elif choice == "2":
                    view_projects(index)
                elif choice == "3":
                    delete_project(index)
                elif choice == "4":
                    edit_projects(index)
                elif choice == "5":
                    search_project(index)   
                elif choice == "6":
                    break
            else:
                break
    elif choice == "3":
        print("Exiting ...")
        break
    else:
        print("Invalid Choice")                
    

