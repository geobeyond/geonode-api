from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql.base import UUID
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from uuid import uuid4

from app.db.base_class import Base
from app.db_models.user import User
from app.models.job import statusEnum
from app.core.config import StatusMessage


class Job(Base):

    __tablename__ = 'job'

    jid         = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )
    status      = Column(
        String,
        index=True,
        default=statusEnum.ACCEPTED.value
    )
    message     = Column(
        String,
        index=True,
        default=StatusMessage.ACCEPTED.value
    )
    progress      = Column(Integer, default=0)
    links         = Column(postgresql.JSONB, default=[])
    inputs        = Column(postgresql.JSONB, default=[])
    outputs       = Column(postgresql.JSONB, default=[])
    result        = Column(postgresql.JSONB)
    created_at    = Column(DateTime, default=func.now(), nullable=False)
    updated_at    = Column(DateTime, onupdate=func.now())
    process_id    = Column(Integer, ForeignKey("process.pid"))
    owner_id      = Column(Integer, ForeignKey("user.id"))
    owner         = relationship("User", back_populates="jobs")
    process_ref   = relationship("Process", back_populates="jobs")