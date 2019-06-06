from pydantic import Union
from app.models.common import (
    dataDescriptionType,
    complexDataType,
    literalDataType,
    boundingBoxDataType
)


class outputDescription(dataDescriptionType):
    output: Union[complexDataType, literalDataType, boundingBoxDataType]