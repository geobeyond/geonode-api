from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.db_models.job import Job


def get_multi_by_process(
    db_session: Session,
    *,
    process_id: int,
    skip=0,
    limit=100
) -> List[Optional[Job]]:
    return (
        db_session.query(Job)
        .filter(Job.process_id == process_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_multi_by_process_by_owner(
    db_session: Session,
    *,
    process_id: int,
    owner_id: int,
    skip=0,
    limit=100
) -> List[Optional[Job]]:
    return (
        db_session.query(Job)
        .filter(Job.owner_id == owner_id)
        .filter(Job.process_id == process_id)
        .offset(skip)
        .limit(limit)
        .all()
    )