from dataclasses import dataclass
from model.data_entities.comment import Comment
from model.data_entities.user import User
from typing import List

@dataclass
class Chat:
    id: str
    members: List[User]
    messages: List[Comment]