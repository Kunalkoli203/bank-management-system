#user registeration signin signup
from database import *
import random
def signup():
    username = input("create username: ")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("username already exist")
        signup()
    else:
        print("username is available please proceed")
        password = input("enter your password")
        name = input("enter your name: ")
        age=input("enter your age: ")
        city= input("enter your city: ")
        while True:
            #account_number =generate_unique_account_number()
            account_number=int(random.randint(10000000, 99999999))
            #random.randint(10000000, 99999999)
            #print(account_number)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print(account_number)
                break



