from abc import ABC, abstractmethod
from model.data_entities.user import User


class IAuthRepository(ABC):
    @abstractmethod
    def getUserByEmail(self, email: str) -> User:
        pass

    @abstractmethod
    def createUser(self, user: User):
        pass

    @abstractmethod
    def updateUser(self, user: User):
        pass

    @abstractmethod
    def deleteUser(self, user: User):
        pass