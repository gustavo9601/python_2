class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password

    def get_id_usuario(self):
        return self.__id_usuario

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return (f'id_usuario: {self.__id_usuario} | username: {self.__username} | password: {self.__password}')
