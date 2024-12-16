from dataclasses import dataclass
from model.data_entities.user import User
from model.data_entities.content import Content
from datetime import datetime

@dataclass
class Comment:
    chatId: str
    author: User
    content: Content
    dateTime: datetime