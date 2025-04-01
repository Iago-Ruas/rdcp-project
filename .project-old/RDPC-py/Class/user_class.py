import uuid
from decouple import config
from cryptography.fernet import Fernet
from schemas import UserCreator


class User(UserCreator):

    def __init__(self):
        self._id = uuid.uuid4()
        self._name = None
        self._email = None
        self._pswd = None
        self._type = None

    def __str__(self):
        return f"{self._id} - {self._name} - {self._pswd} - {self._type}"


class Pswd:
    @staticmethod
    def SecurePswd(pswd: str, fernet=Fernet(config("SECRET_KEY").encode())):
        return fernet.encrypt(pswd.encode())

    @staticmethod
    def CheckPswd(
        encripted_pswd: str, pswd: str, fernet=Fernet(config("SECRET_KEY").encode())
    ) -> bool:
        try:
            decrypted_password = fernet.decrypt(encripted_pswd).decode()
            return decrypted_password == pswd
        except Exception as e:
            print(f"Err: {e}")
            return False


class UserBuilder:

    def __init__(self):
        self._user: User = User()

    def SetName(self, user_name: str):
        self._user._name = user_name
        return self

    def SetEmail(self, user_email: str):
        self._user._email = user_email
        return self

    def SetPswd(self, pswd: str):
        self._user._pswd = Pswd.SecurePswd(pswd)
        return self

    def SetUserType(self, type: str):
        self._user._type = type
        return self

    def Build(self):
        return self._user
