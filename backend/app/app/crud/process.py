from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db_models.process import Process
from app.models.process import ProcessCreate, ProcessUpdate


def get(db_session: Session, *, pid: int) -> Optional[Process]:
    return db_session.query(Process).filter(Process.pid == pid).first()


def get_by_id(db_session: Session, *, id: str) -> Optional[Process]:
    return db_session.query(Process).filter(Process.id == id).first()


def get_multi(db_session: Session, *, skip=0, limit=100) -> List[Optional[Process]]:
    return db_session.query(Process).offset(skip).limit(limit).all()


def get_multi_by_owner(
    db_session: Session, *, owner_id: int, skip=0, limit=100
) -> List[Optional[Process]]:
    return (
        db_session.query(Process)
        .filter(Process.owner_id == owner_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create(db_session: Session, *, process_in: ProcessCreate, owner_id: int) -> Process:
    process_in_data = jsonable_encoder(process_in)
    process = Process(**process_in_data, owner_id=owner_id)
    db_session.add(process)
    db_session.commit()
    db_session.refresh(process)
    return process


def update(db_session: Session, *, process: Process, process_in: ProcessUpdate) -> Process:
    process_data = jsonable_encoder(process)
    update_data = process_in.dict(skip_defaults=True)
    for field in process_data:
        if field in update_data:
            setattr(process, field, update_data[field])
    db_session.add(process)
    db_session.commit()
    db_session.refresh(process)
    return process


def remove(db_session: Session, *, pid: int):
    process = db_session.query(Process).filter(Process.pid == pid).first()
    db_session.delete(process)
    db_session.commit()
    return process
