from typing import List
from enum import Enum
from uuid import UUID
from datetime import datetime
from pydantic import Schema, BaseModel, UUID4
from app.models.common import link
from app.models.input import input as input_
from app.models.output import output as output_


class statusEnum(str, Enum):
    ACCEPTED   = 'accepted'
    RUNNING    = 'running'
    SUCCESSFUL = 'successful'
    FAILED     = 'failed'


class statusInfo(BaseModel):
    status: statusEnum = ...
    message: str
    progress: int = Schema(0, gte=0, lte=100)
    links: List[link]


class execute(BaseModel):
    inputs: List[input_]
    outputs: List[output_] = ...


# Shared properties
class JobBase(statusInfo):
    pass

class jobCollection(BaseModel):
    jobs: List[UUID4] = ...


# Properties to receive on process creation
class JobCreate(JobBase):
    pass


# Properties to receive on process update
class JobUpdate(JobBase):
    pass


# Properties shared by models stored in DB
class JobInDBBase(JobBase):
    jid: UUID4 = ...
    owner_id: int
    process_id: int
    created_at: datetime = ...
    updated_at: datetime


# Properties to return to client
class Job(JobInDBBase):
    pass


# Properties properties stored in DB
class JobInDB(JobInDBBase):
    pass