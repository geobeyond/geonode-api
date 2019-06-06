from enum import Enum
from pydantic import Union
from app.models.common import (
    dataDescriptionType,
    complexDataType,
    literalDataType,
    boundingBoxDataType
)


class maxOccursEnum(str, Enum):
    UNBOUNDED = 'unbounded'


class inputDescription(dataDescriptionType):
    input: Union[complexDataType, literalDataType, boundingBoxDataType]
    minOccurs: int
    maxOccurs: Union[int, maxOccursEnum]
