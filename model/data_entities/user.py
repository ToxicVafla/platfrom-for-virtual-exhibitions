from dataclasses import dataclass
from datetime import date
from model.data_entities.permission import Permission

@dataclass
class User:
    name: str
    id: str
    email: str
    password: str
    birthDate: date
    activityPermission: Permission
    componentPermission: Permission