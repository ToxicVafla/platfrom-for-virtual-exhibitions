from abc import ABC, abstractmethod
from model.data_entities.user import User

class IAuthService(ABC):
    @abstractmethod
    def register(self, user: User) -> bool:
        pass

    @abstractmethod
    def login(self, email: str, password: str) -> bool:
        pass

    @abstractmethod
    def updateUser(self, user: User):
        pass

    @abstractmethod
    def deleteUser(self, email: str):
        pass