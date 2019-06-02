import json
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.db_models.user import User as DBUser
from app.models.process import processCollection


router = APIRouter()


@router.get(
    "/processes/",
    operation_id="getProcesses",
    response_model=processCollection,
    status_code=200
)
def read_wps_processes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Retrieve available processes.
    """
    if crud.user.is_superuser(current_user):
        processes = crud.process.get_multi(db, skip=skip, limit=limit)
    else:
        processes = crud.process.get_multi_by_owner(
            db_session=db, owner_id=current_user.id, skip=skip, limit=limit
        )

    mocked_processes = {
        "processes": [
            {
                "id": "buffer",
                "title": "Buffer process",
                "description": "Process that buffers features",
                "keywords": [
                    "buffer"
                ],
                "metadata": [
                    {
                        "role": "self",
                        "href": "https://processing.example.org/processes/buffer"
                    }
                ],
                "links": [
                    {
                        "href": "https://processing.example.org/processes/buffer",
                        "rel": "self",
                        "type": "jjjj",
                        "hreflang": "en",
                        "title": "buffer"
                    }
                ],
                "version": "1.1",
                "jobControlOptions": [
                    "sync-execute",
                    "async-execute"
                ],
                "outputTransmission": [
                    "value",
                    "reference"
                ]
            }
        ]
    }
    return mocked_processes