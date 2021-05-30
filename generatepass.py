import random   
import string  
import secrets   

def get_pass():
    print("How many characters would you like your password to have?")
    num = int(input()) 
    res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))  
    return str(res)
    # print(str(res))
# get_pass()    