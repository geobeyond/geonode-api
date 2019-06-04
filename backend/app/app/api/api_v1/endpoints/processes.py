import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.db_models.user import User as DBUser
from app.models.process import processCollection, Process, ProcessCreate

import logging
logger = logging.getLogger("uvicorn")


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
    return {"processes": processes}


@router.post(
    "/processes/",
    operation_id="createProcess",
    response_model=Process,
    status_code=200,
    include_in_schema=False
)
def create_process(
    *,
    db: Session = Depends(get_db),
    process_in: ProcessCreate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Create new process.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=403, detail="You are not allowed to register processes")
    elif crud.process.get_by_id(db_session=db, id=process_in.id):
        raise HTTPException(status_code=422, detail="The process has been already created")
    process = crud.process.create(db_session=db, process_in=process_in, owner_id=current_user.id)
    return process
