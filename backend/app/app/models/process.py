from typing import List
from enum import Enum
from pydantic import BaseModel, Schema
from app.models.common import link, descriptionType, transmissionMode
from app.models.input import inputDescription
from app.models.output import outputDescription


class jobControlOptions(str, Enum):
    SYNC  = 'sync-execute'
    ASYNC = 'async-execute'


class processSummary(descriptionType):
    id: str = ...
    version: str = ...
    jobControlOptions_: List[jobControlOptions] = Schema(
        None, alias="jobControlOptions"
    )
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