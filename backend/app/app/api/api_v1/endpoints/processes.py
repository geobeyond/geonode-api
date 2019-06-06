import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud
from app.api.utils.db import get_db
from app.api.utils.security import get_current_active_user
from app.db_models.user import User as DBUser
from app.models.process import (
    processCollection,
    Process,
    ProcessCreate,
    processOffering
)


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
    processes = crud.process.get_multi(db, skip=skip, limit=limit)
    if not processes:
        processes = []
    return {"processes": processes}


@router.post(
    "/processes/",
    operation_id="createProcess",
    response_model=Process,
    status_code=200,
    include_in_schema=False
)
def create_wps_process(
    *,
    db: Session = Depends(get_db),
    process_in: ProcessCreate,
    current_user: DBUser = Depends(get_current_active_user),
):
    """
    Create new wps process.
    """
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=403, detail="You are not allowed to register processes")
    elif crud.process.get_by_id(db_session=db, id=process_in.id):
        raise HTTPException(status_code=422, detail="The process has been already created")
    process = crud.process.create(db_session=db, process_in=process_in, owner_id=current_user.id)
    return process


@router.get(
    "/processes/{id}",
    operation_id="getProcessDescription",
    response_model=processOffering,
    status_code=200
)
def read_wps_process(
    *,
    db: Session = Depends(get_db),
    id: str,
):
    """
    Get a process description.
    """
    process = crud.process.get_by_id(db_session=db, id=id)
    if not process:
        raise HTTPException(status_code=404, detail=f"The process with id {id} does not exist.")
    return {"process": process}
