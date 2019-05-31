from fastapi import APIRouter

from app.models.conformance import Conformance, conformanceClassesEnum, reqClasses


router = APIRouter()


@router.get(
    "/conformance/",
    operation_id="getRequirementsClasses",
    response_model=Conformance,
    status_code=200
)
def read_wps_api_conformance():
    """
    Retrieve API conformance definition.
    """
    classes = [
        class_value.value for class_name, class_value in conformanceClassesEnum
        .__members__
        .items()
    ]
    return reqClasses(conformsTo=classes)
