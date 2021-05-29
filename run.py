#!/usr/bin/env python3.8
from user_class import User  # Importing the user class
from credentials_class import Credentials
from generatepass import *
    
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
    return Credentials.display_credentials()

# main
def main():
    
    print("Hello, Welcome to PassworLocker. Create an account to save your passwords")
    print('\n')
 
   

    while True:
        print("...............")
        print("Choose a shortcode to proceed : ca - create an account, ex - to exit")
        print("...............")
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
                                print('user name')
                                entered_username= input()
                                print("Your password")
                                entered_password = input()                     
              
        break

    while True:
        print('\n')
        print(f'Welcome back  {entered_username}')
        print('Use these codes to navigate: cc -create a credential, dc-display credentials, dl-delete credentials, sc- search account by name, ex-exit')
        short_code = input('Enter your choice: ').lower()

        if short_code == "ex": 
            print('Goodbye')
            break
        elif short_code == "cc":
            print('Enter your credentials details')
            print("Enter site name")
            account_name= input()
            print("Enter username")
            username= input()
            print("Enter email")
            email = input()
            while True:
                print("Do you want to generate a password?")
                print("Choose 'y' for yes or 'n' for no, 'ex' to exit")
                pswd_choice = input().lower()

                if pswd_choice == 'n':
                    print("Enter your password")
                    password = input()
                    break
                elif pswd_choice==   'y' :
                    password = get_pass()
                    print ("Your generated password is " + password)
                    break
                elif pswd_choice == 'ex':
                    break 
                else:   
                    print('Invalid option')              
            save_credentials(create_credentials(account_name, username, email, password))
            print(f'Your credential has been created: Site name: {account_name} - Email: {email} -Password: {password}')
        elif short_code == "dc": 
            if display_credentials():
                print('Here is a list of all your contacts')
                print('\n')
                for credential in display_credentials():
                    print(
                        f'{credential.account_name}: \nuser name: {credential.username},  Email: {credential.email}  password: {credential.password}')
            else:
                print("You dont seem to have any credentials saved yet") 
        elif short_code == "sc":
            print("Enter an account name to search")
            account_name = input()
            if find_credentials(account_name):
                search_credentials = find_credentials(account_name)
                print(f"{search_credentials.account_name} {search_credentials.username} {search_credentials.password}")
            else:
                print("That contact does not exist")    

        elif short_code == "dl":
            print("Enter account name you would like to delete")
            search_credentials = input()
            if  find_credentials(account_name):
                print("Please wait ...")
                check_account = find_account(search_account)
                delete_account(check_account)
                print(
                    f"Account {check_account.account_name}deleted successfully")
            else:
                print('\n')
                print("dlfailed")

         

                
                              

                                         

if __name__ == '__main__':
    main()    
