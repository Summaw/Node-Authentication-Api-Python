import requests
import json
import os
from time import sleep




LOGIN = 'http://localhost:2400/api/auth/login'

def Menu():
    logo()
    print("[?] What would you like to do?\n")
    print("[1] Login")
    print("[2] Sign Up")
    x = input("Please select an option\n")

    if x == "1":
        os.system('cls')
        login()
    if x == "2":
        os.system('cls')
        signup()
    else:
        os.system('cls')
        logo()
        print("You failed to select an option please reopen the program and try again.")

def signup():
    logo()
    a = input("[?] What is your email?\n")
    b = input("[?] What is your password?\n")
    payload = {
    'email': a,
    'password': b
    }
    s = requests.session()
    response = s.post('http://localhost:2400/api/auth/signup', json=payload)
    
    if response.status_code == 200:
        print('[!] You have successfully signed up!')
        sleep(5)
    else:
        print(response.content)
        sleep(5)
        exit()


def login():
    logo()
    a = input("[1] What is your email?\n")
    b = input("[2] What is your password?\n")

    payload = {
    'email': a,
    'password': b
    }
    s = requests.session()
    response = s.post(LOGIN, json=payload)
    
    if response.status_code == 200:
        print('[!] Successfully logged you in!')
        sleep(5)
    else:
        print(response.content)
        sleep(5)


def logo():
    print('''
        Developer: Summer
        ''')


if __name__ == "__main__":
    Menu()
