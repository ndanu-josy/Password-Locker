class Credentials:    
    """
    Class that generates new instances of user credentials
    """

    credentials_list = []

    def __init__(self, account_name, username, email, password):
        
        '''
        __init__ method that helps us define properties for our objects.

        '''
        self.account_name = account_name
        self.username = username
        self.email = email
        self.password = password
   
    def save_credentials(self):
        '''
        A function to save credentials
        '''
        Credentials.credentials_list.append(self) 

    def delete_credentials(self):
        '''
        Delete user credentials
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_accountname(cls, account_name): 
        '''
        Method that searches account by name and returns the details
        '''  

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list


