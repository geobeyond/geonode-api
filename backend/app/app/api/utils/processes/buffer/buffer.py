from typing import List
from app.models.input import input as Input
from app.models.output import output as Output
from app.models.result import (
    outputInfo as OutputInfo,
    result as Result
)


class Buffer:
    """Buffer example class

    Parameters
    ----------
    inputs: list of Output
        inputs of the process
    outputs: list of Input
        outputs of the process, none by default
    """

    def __init__(self, inputs: List[Input], outputs: List[Output]):
        self.inputs = inputs
        self.outputs = outputs

    @property
    def result(self) -> Result:
        return self.__result

    @result.setter
    def result(self, value: Result):
        """Set new value for result

        Parameters
        ----------
        value : Result
            Assign new result to the Buffer instance
        """
        self.__result = value

    def run(self):
        """
        Perform buffering on vector data.
        """
        # performs the buffering on a point-based geojson
        # https://gist.githubusercontent.com/francbartoli/048fde7f214e5747c3faad0745723004/raw/830a52b8234b92d08c7c2b79f7f585a932ed4e7b/map.geojson
        mock_feature = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {
                            "city": "Vacone",
                            "name": "Castello di Vacone",
                            "type": "Heritage"
                        },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [
                            12.644287347793579,
                            42.38511889311794
                            ]
                        }
                    }
                ]
            }
        res = mock_feature
        self.__result = Result(outputs=List[OutputInfo(id="result", value=dict(inlineValue=res))])