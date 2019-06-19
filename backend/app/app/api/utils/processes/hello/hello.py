from typing import List
from app.models.result import (
    outputInfo as OutputInfo,
    result as Result
)


hello = "hello world"

def getResult() -> Result:
    result = Result(outputs=[OutputInfo(
        id="result", value=dict(inlineValue=hello)
    )])
    return result
