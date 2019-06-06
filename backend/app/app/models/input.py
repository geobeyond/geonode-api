from pydantic import Union
from app.models.common import (
    dataDescriptionType,
    complexDataType,
    literalDataType,
    boundingBoxDataType
)


class inputDescription(dataDescriptionType):
    input: Union[complexDataType, literalDataType, boundingBoxDataType]
    minOccurs: int
    maxOccurs: int
