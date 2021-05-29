#!/usr/bin/env python3.8
from user_class import User  # Importing the user class


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
    print("Confirm password ....")
    confirm_password = input()
    
    while confirm_password != password:
                print("Password did not match")
                print("Enter password again")
                password = input()
                print("Confirm password ....")
                confirm_password = input()
    else:
                save_user(create_user(username, password))
                print(f'Congratulations 🎉, New Account has been created for: {username} using password: {password}')
                print("proceed to login")
                print("username")
                entered_username = input()
                print("your password")
                entered_password = input()

    if          entered_username!= username or entered_password != password:
                print("Invalid username or password")
                print('first name')
                entered_username= input()
                print("Your password")
                entered_password = input()
                 
        
    print(f'Welcome back  {entered_username} 😍. please choose an option to continue')

if __name__ == '__main__':
    main()    
