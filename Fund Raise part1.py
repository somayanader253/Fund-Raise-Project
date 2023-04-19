import re
import os
import datetime

def register_user():

    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")

    def validate_name(name):
        for char in name:
            if not(char.isalpha()) and not(char.isspace()):
               return False
        return True
    
    if not validate_name(firstname) or not validate_name(lastname):
        print("Invalid name. Please enter letters only.")


    phone = input("Enter your phone number: ")

    def validate_phone(phone):
        if len(phone) != 11 or not phone.startswith('01'):
           return False
    
        if not phone.isdigit():
           return False
    
        return True

    if not validate_phone(phone):
        print("Invalid mobile number. Please enter a valid mobile number")


    
    email = input("Enter your email address: ")
    
    def validate_email(email):
        if "@" in email and ".com" in email:
            return True
        else:
            return False
    
    if not validate_email(email):
        print("Invalid email address. Please enter a valid email address.")
    
    password = input("Enter your password: ")
    confirm_password = input("Re-enter your password: ")
    
    def validate_password(password, confirm_password):
        if len(password) < 8:
           print("Password must be at least 8 characters.")
           return False

        if password != confirm_password:
           print("Password and confirmation do not match.")
           return False

        return True
    
    if validate_password(password, confirm_password):
        print("Password is valid.")
    else:
        print("Password is invalid.")
    

    print("Registration successful!")
#register_user()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Logged in successfully!")

while True:
    print("Welcome! Choose an option:")
    print("1. Login")
    print("2. Register")
    option = input("Enter your choice (1 or 2): ")
    if option == "1":
        login()
        break
    elif option == "2":
        register_user()
        break
    else:
        print("Invalid option. Please choose 1 or 2.")

# def validate_date(start_time, end_time):
#     if end_time <= start_time:
#         return False
#     if start_time <= datetime.datetime.now() or end_time <= datetime.datetime.now():
#         return False
#     return True


# def validate_money(target):
#     pattern = r'^\d+(\.\d{1,2})?EGP' 
#     if not re.match(pattern, target):
#         return False
#     if target.startswith('0'):
#         return False  # Disallow leading zeros
#     return True
