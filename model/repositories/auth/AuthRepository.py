from typing import Dict
from model.data_entities.user import User
from model.repositories.auth.IAuthRepository import IAuthRepository

class AuthRepository(IAuthRepository):
    def __init__(self):
        self.users: Dict[str, User] = {}

    def getUserByEmail(self, email: str) -> User:
        return self.users.get(email)

    def createUser(self, user: User):
        if user.email not in self.users:
            self.users[user.email] = user
        else:
            raise ValueError(f"User with email {user.email} already exists.")

    def updateUser(self, user: User):
        for existing_user_email, existing_user in self.users.items():
            if existing_user.email == user.email:
                del self.users[existing_user_email]

                self.createUser(user)
                break

    def deleteUser(self, user: User):
        if user.email in self.users:
            del self.users[user.email]
        else:
            raise ValueError(f"User with email {user.email} does not exist.")