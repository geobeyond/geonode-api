from typing import List
from enum import Enum
from pydantic import BaseModel, UrlStr
from app.models.common import link


class metadataType(BaseModel):
    role: str = None
    href: str = None


class descriptionType(BaseModel):
    id: str = ...
    title: str = None
    description: str = None
    keywords: List[str] = None
    metadata: List[metadataType] = None


class jobControlOptionsType(str, Enum):
    SYNC  = 'sync-execute'
    ASYNC = 'async-execute'


class transmissionMode(str, Enum):
    VALUE     = 'value'
    REFERENCE = 'reference'


class processSummary(descriptionType):
    id: str = ...
    version: str = ...
    jobControlOptions: List[jobControlOptionsType]
    outputTransmission: List[transmissionMode]
    links: List[link]


# Shared properties
class ProcessBase(BaseModel):
    processes: List[processSummary] = []


class processCollection(ProcessBase):
    pass


# Properties to receive on process creation
class ProcessCreate(ProcessBase):
    pass


# Properties to receive on process update
class ProcessUpdate(ProcessBase):
    pass


# Properties shared by models stored in DB
class ProcessInDBBase(ProcessBase):
    pid: int
    owner_id: int
