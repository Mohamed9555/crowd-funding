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
