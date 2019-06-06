from typing import List
from enum import Enum
from pydantic import BaseModel, Schema, UrlStr, Union


class link(BaseModel):
    href: UrlStr = ...
    rel: str = None
    type: str = None
    hreflang: str = None
    title: str = None


class metadataType(BaseModel):
    role: str = None
    href: str = None


class descriptionType(BaseModel):
    id: str = ...
    title: str = None
    description: str = None
    keywords: List[str] = None
    metadata_: List[metadataType] = Schema(None, alias="metadata")


class dataDescriptionType(descriptionType):
    pass


class supportedCRS(BaseModel):
    crs: str
    default: bool = False


class boundingBoxDataType(BaseModel):
    supportedCRS_: List[supportedCRS] = Schema(None, alias="supportedCRS")


class literalDataType(BaseModel):
    literalDataDomains: List[literalDataDomain] = None


class anyValue(BaseModel):
    anyValue_: bool = Schema(None, alias="anyValue")


class rangeClosureEnum(str, Enum):
	CLOSED     = 'closed'
	OPEN       = 'open'
	OPENCLOSED = 'open-closed'
	CLOSEDOPEN = 'closed-open'


class Range(BaseModel):
    minimumValue: str
    maximumValue: str
    spacing: str
    rangeClosure: rangeClosureEnum


class allowedRanges(BaseModel):
    allowedRanges_: List[Range] = Schema(None, alias="allowedRanges")


class datatypeType(BaseModel):
    name: str = ...
    reference: UrlStr


class uomType(BaseModel):
    name: str = ...
    reference: UrlStr


class literalDataDomain(BaseModel):
    valueDefinition: Union[
        List[Union[str, Range]], # allowedValues
        allowedRanges,
        anyValue,
        UrlStr # valuesreference
    ]
    defaultValue: str = None
    dataType: datatypeType
    uom: uomType


class literalDataType(BaseModel):
    literalDataDomains: List[literalDataDomain]


class format(BaseModel):
    mimeType: str = ...
    schema_: str = Schema(None, alias="schema")
    encoding: str


class formatDescription(format):
    maximumMegabytes: int
    default: bool = False


class complexDataType(BaseModel):
    formats: List[formatDescription] = ...
