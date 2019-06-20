from typing import List
from pydantic import Schema, BaseModel, Union


class referenceValue(BaseModel):
    href: str


class inlineValue(BaseModel):
    inlineValue_: Union[dict, str, int, bool] = Schema(
        ..., alias="inlineValue"
    )


class valueType(BaseModel):
    pass


class outputInfo(BaseModel):
    id: str = ...
    value: Union[inlineValue, referenceValue] = ...


class result(BaseModel):
    outputs: List[outputInfo] = ...