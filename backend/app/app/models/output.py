from pydantic import Schema, BaseModel, Union
from app.models.common import (
    dataDescriptionType,
    complexDataType,
    literalDataType,
    boundingBoxDataType
)
from app.models.common import transmissionMode, format as Format


class dataType(BaseModel):
    format_: Format = Schema(None, alias="format")


class outputDescription(dataDescriptionType):
    output: Union[complexDataType, literalDataType, boundingBoxDataType]


class output(dataType):
    id: str
    transmissionMode_: transmissionMode = Schema(
        None, alias="transmissionMode"
    )
