from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Process(Base):
    pid                = Column(Integer, primary_key=True, index=True)
    id                 = Column(String, unique=True, index=True)
    title              = Column(String, index=True)
    description        = Column(String, index=True)
    keywords           = Column(postgresql.JSONB)
    metadata_          = Column(postgresql.JSONB)
    version            = Column(String, index=True)
    jobControlOptions  = Column(postgresql.JSONB)
    outputTransmission = Column(postgresql.JSONB)
    links              = Column(postgresql.JSONB)
    inputs             = Column(postgresql.JSONB)
    outputs            = Column(postgresql.JSONB)
    owner_id           = Column(Integer, ForeignKey("user.id"))
    owner              = relationship("User", back_populates="processes")
    jobs               = relationship("Job", back_populates="process")
