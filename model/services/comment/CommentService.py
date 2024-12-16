from typing import List
from model.services.comment.ICommentService import ICommentService
from model.data_entities.chat import Chat
from model.data_entities.comment import Comment
from model.repositories.comment.CommentRepository import CommentRepository


class CommentService(ICommentService):
    def __init__(self):
        self.commentRepository = CommentRepository()

    def getComments(self, id: str) -> List[Comment]:
        comments = self.commentRepository.getComments(id)
        return comments

    def createChat(self, chat: Chat):
        self.commentRepository.createChat(chat)

    def addComment(self, comment: Comment):
        self.commentRepository.addComment(comment)

    def deleteComment(self, comment: Comment):
        self.commentRepository.deleteComment(comment)