class User:
    '''
    Class that creates instances of user details.
    '''
    user_data =[]

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_data
        '''

        User.user_data.append(self)
        



