import unittest # Importing the unittest module
from user_Class import User # Importing the contact class

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


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"ndanu-josy")
        self.assertEqual(self.new_user.password,"2021")        


if __name__ == '__main__':
    unittest.main()     