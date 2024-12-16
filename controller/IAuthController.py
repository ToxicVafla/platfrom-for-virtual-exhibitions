from abc import ABC, abstractmethod

from flask.ctx import RequestContext

from model.data_entities.user import User


class IAuthController(ABC):
    @abstractmethod
    def profileGet(self, email: str) -> User:
        pass

    @abstractmethod
    def register(self, email: str, password: str) -> User:
        pass

    @abstractmethod
    def login(self, email: str, password: str) -> User:
        pass

    @abstractmethod
    def updateUser(self, email: str, password: str, email_new: str, password_new: str):
        pass

    @abstractmethod
    def deleteUser(self, context: RequestContext, user: User):
        pass

    @abstractmethod
    def validateEmail(self, context: RequestContext, email: str) -> bool:
        pass

    @abstractmethod
    def validatePassword(self, context: RequestContext, password: str) -> bool:
        pass