#!/usr/bin/env python3.8
from user_Class import User  # Importing the user class


def create_user(username, password):
    '''
    Funcion to create a new user
    '''
    new_user = User(username, password)
    return new_user


def save_user(user):
    '''
    Function to save user 
    '''
    user.save_user()


def check_existing_user(username, password):
    '''
    Function to check if a user account exists
    '''
    return User.user_exist(username, password)


def main():
    print("Hello, Welcome to PassworLocker. Create an account to save your passwords")
    print('Enter your username')
    username = input()
    print("What's your password")
    password = input()


if __name__ == '__main__':
    main()    
