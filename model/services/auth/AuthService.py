from model.data_entities.user import User
from model.services.auth.IAuthService import IAuthService
from model.repositories.auth.AuthRepository import AuthRepository


class AuthService(IAuthService):
    def __init__(self):
        self.authRepository = AuthRepository()

    def register(self, user: User) -> bool:
        try:
            self.authRepository.createUser(user)
            return True
        except ValueError as e:
            return False

    def login(self, email: str, password: str) -> bool:
        user = self.authRepository.getUserByEmail(email)
        if user and user.password == password:
            return True
        else:
            return False

    def updateUser(self, user: User):
        self.authRepository.updateUser(user)

    def deleteUser(self, email: str):
        user = self.authRepository.getUserByEmail(email)
        if user:
            self.authRepository.deleteUser(user)