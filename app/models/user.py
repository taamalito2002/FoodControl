class User:
    users = []  # Lista simulando la base de datos

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def register(cls, username, password):
        # Verificar si el usuario ya existe
        for user in cls.users:
            if user.username == username:
                return False
        # Crear nuevo usuario
        cls.users.append(User(username, password))
        return True

    @classmethod
    def authenticate(cls, username, password):
        for user in cls.users:
            if user.username == username and user.password == password:
                return True
        return False
