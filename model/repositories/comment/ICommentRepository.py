from abc import ABC, abstractmethod
from typing import List
from model.data_entities.comment import Comment
from model.data_entities.chat import Chat


class ICommentRepository(ABC):
    @abstractmethod
    def getComments(self, id: str) -> List[Comment]:
        pass

    @abstractmethod
    def createChat(self, chat: Chat):
        pass

    @abstractmethod
    def addComment(self, comment: Comment):
        pass

    @abstractmethod
    def deleteComment(self, comment: Comment):
        pass