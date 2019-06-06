from typing import List
from enum import Enum
from pydantic import BaseModel, UrlStr, Schema, Json
from app.models.common import link, descriptionType
from app.models.input import inputDescription
from app.models.output import outputDescription


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
class ProcessBase(processSummary):
    inputs: List[inputDescription]
    outputs: List[outputDescription]


class processCollection(BaseModel):
    processes: List[processSummary] = []


class processOffering(BaseModel):
    process: ProcessBase = ...


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