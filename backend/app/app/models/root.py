from typing import List
from enum import Enum
from pydantic import BaseModel
from app.models.common import link


class root(BaseModel):
    links: List[link]


class Link(root):
    pass