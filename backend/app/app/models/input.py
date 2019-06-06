from enum import Enum
from pydantic import Schema, BaseModel, Union
from app.models.common import (
    dataDescriptionType,
    complexDataType,
    literalDataType,
    boundingBoxDataType
)


class maxOccursEnum(str, Enum):
    UNBOUNDED = 'unbounded'


class inputDescription(dataDescriptionType):
    input_: Union[
        complexDataType,
        literalDataType,
        boundingBoxDataType
    ] = Schema(None, alias="input")
    minOccurs: int
    maxOccurs: Union[int, maxOccursEnum]


class input(BaseModel):
    id_: str = Schema(..., alias="id")
    input_: Union[
        complexDataType,
        literalDataType,
        boundingBoxDataType
    ] = Schema(None, alias="input")
