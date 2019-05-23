from typing import List
from enum import Enum
from pydantic import BaseModel, UrlStr


class conformanceClassesEnum(UrlStr, Enum):
    CORE = 'http://www.opengis.net/spec/WPS/2.0/req/service/binding/rest-json/core'
    OAS3 = 'http://www.opengis.net/spec/WPS/2.0/req/service/binding/rest-json/oas30'
    HTML = 'http://www.opengis.net/spec/WPS/2.0/req/service/binding/rest-json/html'


class reqClasses(BaseModel):
    conformsTo: List[conformanceClassesEnum] = ...


class Conformance(reqClasses):
    pass
