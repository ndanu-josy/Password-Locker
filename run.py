#!/usr/bin/env python3.8
from user_class import User  # Importing the user class
from credentials_class import Credentials
    
    #user
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


    #Credentials

def create_credentials(account_name, username, email, password):
    '''
    Function to crreate new credentials
    '''  
    new_credentials =Credentials(account_name, username, email, password)  
    return new_credentials

def  save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete credentials
    '''
    credentials.delete_credentials()   

def find_credentials(account_name):
    '''
    Function that finds credentials by account name
    '''
    return Credentials.find_by_accountname(account_name)

def display_credentials():
    '''
    Function that displays all saved credentials 
    '''


# main
def main():
    print("Hello, Welcome to PassworLocker. Create an account to save your passwords")
    print("...............")
    print('\n')

    while True:
        print("Choose a shortcode to proceed : ca - create an account, ex - to exit")
        short_code = input('Enter a choice: ').lower()

        if short_code == 'ex':
            print("Goodbye")
            break
        elif short_code == 'ca':

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
                    print(f'Congratulations, New Account has been created for: {username} using password: {password}')
                    print("Choose a shortcode to proceed : lg - login, ex-exit")
                    short_code = input('Enter a choice: ').lower()

                    if short_code == 'ex':
                        print("Goodbye")
                        break
                    elif short_code == 'lg':
                 
                            print("proceed to login")
                            print("username")
                            entered_username = input()
                            print("your password")
                            entered_password = input()

                    if  entered_username!= username or entered_password != password:
                                print("Invalid username or password")
                                print('first name')
                                entered_username= input()
                                print("Your password")
                                entered_password = input()                        
                            
                    
        
        break

    while True:
        print('\n')
        print(f'Welcome back  {entered_username}')
        print('Use these codes to navigate: nc -create a credential, dc-dipslay credentials, cp-copy credential, ex-exit')
        short_code = input('Enter your choice: ').lower()

if __name__ == '__main__':
    main()    
