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
        self.new_credentials= Credentials("Instagram", "ndanu-josy","jos@me.com","nd@nu")

    #test 4
    def test_init(self):
        '''
        test_init test case to test if the objects is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name,"Instagram")
        self.assertEqual(self.new_credentials.username, "ndanu-josy")  
        self.assertEqual(self.new_credentials.email, "jos@me.com")  
        self.assertEqual(self.new_credentials.password, "nd@nu") 

    #test 5
    def test_save_credentials(self): 
        '''
        test_save_credentials test case to test if the credentials object is saved into
        the credentials list
        '''

        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    #teardown
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list=[]

    #test 6
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials() 
        test_credentials = Credentials("Instagram", "ndanu-josy","jos@me.com","nd@nu")
        test_credentials.save_credentials()

        self.assertEqual(len(Credentials.credentials_list),2)


if __name__ == '__main__':
    unittest.main()     