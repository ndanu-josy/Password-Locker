class Credentials:    
    """
    Class that generates new instances of user credentials
    """

    credentials_list = []

    def __init__(self, account_name, username, password):
        
        '''
        __init__ method that helps us define properties for our objects.

        '''
        self.account_name = account_name
        self.username = username
        self.password = password



