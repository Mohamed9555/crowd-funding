import getpass
import re
from fileop import *

def check_name(position):
    if position == "first":
        name = input("Enter first name: ")
    else: 
        name = input("Enter last name: ")
    while True:
        if len(name) == 0:
            print("Name can't be empty")
            name = input("Try again: ")
        pattern = re.match("^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$", name)
        if pattern:
            return name
        else:
            print("Invalid name")
            name = input("Try again: ")

def check_mail():
    mail = input("Enter email: ")
    while True:
        if len(mail) == 0:
            print("mail can't be empty")
            mail = input("Try again: ")
        pattern = re.match(r'\b[A-Za-z0-9._%+-]{1,64}@[A-Za-z0-9.-]{2,192}\.[A-Z|a-z]{2,63}\b', mail)
        if pattern:
            return mail
        else:
            print("Invalid mail")
            mail = input("Try again: ")

def check_if_mail_exist(email):
    data = load_data()
    for item in data:
        if email == item["email"]:
            return True
    return False

def check_if_pass_exist(password):
    data = load_data()
    for item in data:
        if password == item["password"]:
            return True
    return False


def check_password():
    password = getpass.getpass("Enter password: ")
    while True:
        pattern = re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)
        if pattern:
            return password
        else:
            print("passowrd should contain minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character")
            password = getpass.getpass("Try Again: ")

def check_phone():
    phone_num = input("Enter phone number: ")
    while True:
        if len(phone_num) == 0:
            print("phone number can't be empty")
            phone_num = input("Try again: ")
        pattern = re.match(r'01[0512]\d{8}$', phone_num)
        if pattern:
            return phone_num
        else:
            print("Invalid phone number")
            phone_num = input("Enter phone number: ")

def check_date(end_or_start):
    date = input(f"Enter {end_or_start} date in Format yyyy-mm-dd (eg.1605-11-05): ")    
    while True:
        pattern = re.match("([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))", date)
        if pattern:
            return date
        else:
            print("Invalid date")
            date = input(f"Enter {end_or_start} date in Format yyyy-mm-dd (eg.1605-11-05): ")    

