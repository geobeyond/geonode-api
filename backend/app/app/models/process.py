from typing import List
from enum import Enum
from pydantic import BaseModel, UrlStr, Schema, Json
from app.models.common import link


class metadataType(BaseModel):
    role: str = None
    href: str = None


class descriptionType(BaseModel):
    id: str = ...
    title: str = None
    description: str = None
    keywords: List[str] = None
    metadata_: List[metadataType] = Schema(None, alias="metadata")


# class descriptionTypeOut(BaseModel):
#     id: str = ...
#     title: str = None
#     description: str = None
#     keywords: Json = None
#     metadata_: Json = Schema(None, alias="metadata")


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


# class processSummaryOut(descriptionTypeOut):
#     id: str = ...
#     version: str = ...
#     jobControlOptions: Json
#     outputTransmission: Json
#     links: Json


# Shared properties
class ProcessBase(processSummary):
    pass


class processCollection(BaseModel):
    processes: List[processSummary] = []


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


# Properties to return to client
class Process(ProcessInDBBase):
    pass


# Properties properties stored in DB
class ProcessInDB(ProcessInDBBase):
    pass