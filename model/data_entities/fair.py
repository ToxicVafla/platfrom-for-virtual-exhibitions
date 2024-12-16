from dataclasses import dataclass
from model.data_entities.activity import Activity
from model.data_entities.presentation import Presentation
from typing import List

@dataclass
class Fair(Activity):
    presentations: List[Presentation]