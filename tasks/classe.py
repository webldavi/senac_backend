class User:
    __teste = 'dwdw'
    def __init__(self, username, password, email, phone):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def get_username(self):
        return self.username

    @property
    def get_teste(self):
        return self.__teste

    @get_teste.setter
    def set_teste(self, teste):
        self.__teste = teste
        
    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def alter_password(self, password):
        self.password = password

    def alter_email(self, email):
        self.email = email

    def alter_phone(self, phone):
        self.phone = phone

    def alter_username(self, username):
        self.username = username

    def alter_username(self, username):
        self.username = username
