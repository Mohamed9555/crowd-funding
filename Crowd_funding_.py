from components import *
from fileop import *
from project_functions import *

def create_user():
    first_name = check_name("first")
    last_name = check_name("last")
    email = check_mail()
    email = email.lower()
    while check_if_mail_exist(email):
        print("Email Already Exists ")
        email = check_mail()
    password = check_password()
    while check_if_pass_exist(password):
        print("Try Different Password")
        password = check_password()
    confirm_password = getpass.getpass("Confirm password: ") # <<<< go back here
    while password != confirm_password:
        confirm_password = getpass.getpass("password doesn't match try again: ") # <<<< go back here
    phone_num = check_phone()
    
    user_data = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email,
        "password" : password,
        "phone_num" : phone_num,
        "projects" : [] 
    }   
    
    save_data(user_data)

# create_user()

def login():
    data = load_data()
    flag = 0
    exist =  False
    email = input("Enter Email: ")
    email = email.lower()
    name = ""
    for index, item in enumerate(data):
        if item["email"] == email:
            flag = 1
            password = getpass.getpass("Enter password: ")
            if password == item["password"]:
                print("logged in as", item["first_name"])
                exist = True
                name = item["first_name"] + " " + item["last_name"]
                return name, index, exist
            else:
                print("Wrong password")
                return name, index, exist
    if flag == 0:
        print("wrong email")
        return name, index, exist

# login()



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
    

