from typing import List, Dict
from model.data_entities.comment import Comment
from model.data_entities.chat import Chat
from model.repositories.comment.ICommentRepository import ICommentRepository

class CommentRepository(ICommentRepository):
    def __init__(self):
        self.chats: Dict[str, Chat] = {}

    def getComments(self, id: str) -> List[Comment]:
        chat = self.chats.get(id)
        return chat.messages

    def createChat(self, chat: Chat):
        if chat.id not in self.chats:
            self.chats[chat.id] = chat
        else:
            raise ValueError(f"Chat with id {chat.id} already exists.")

    def addComment(self, comment: Comment):
        chat = self.chats.get(comment.chatId)
        if chat:
            chat.messages.append(comment)
        else:
            raise ValueError(f"Chat with id {comment.chatId} does not exist.")

    def deleteComment(self, comment: Comment):
        chat = self.chats.get(comment.chatId)
        if chat:
            chat.messages.remove(comment)
        else:
            raise ValueError(f"Comment not found in chat with id {comment.chatId}.")