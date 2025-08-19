#user registeration signin signup
from database import *
import random
def signup():
    username = input("create username: ")
    temp = cursor.execute(f"SELECT username FROM customers where username = '{username}';")
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
            account_number = random.randint(10000000, 99999999)
            temp = db_query(f"SELECT account_number FROM customers WHERE account_numer = '{account_number}';")
            if temp:
                continue
            else:
                pass



