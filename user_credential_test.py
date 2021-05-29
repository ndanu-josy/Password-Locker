import unittest # Importing the unittest module
from user_class import User # Importing the user class
from credentials_class import Credentials # Importing the credentials class

#user test class
class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class 

    Args: 
    unittest.TestCase: helps in creating test cases
    '''   
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("ndanu-josy", "2021") # create user object

    #test 1
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"ndanu-josy")
        self.assertEqual(self.new_user.password,"2021")  

    #test 2
    def test_save_user(self):
        '''
        test case to test if the user object is saved
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_data),1)

    #test 3
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_user.save_user()
        test_user= User ("ndanu-josy", "2021") # new user
        test_user.save_user()

        user_exists = User.user_exist("ndanu-josy", "2021")
        self.assertTrue(user_exists)

      
    #Credentials test class
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviors.
     '''
    def setUp(self):
        '''
        Function to create credentials before each test
        '''
        self.new_credential= Credentials("Instagram", "ndanu-josy","jos@me.com","nd@nu")

    #test 4
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_name,"Instagram")
        self.assertEqual(self.new_credential.username, "ndanu-josy")  
        self.assertEqual(self.new_credential.email, "jos@me.com")  
        self.assertEqual(self.new_credential.password, "nd@nu")  
        

 

if __name__ == '__main__':
    unittest.main()     