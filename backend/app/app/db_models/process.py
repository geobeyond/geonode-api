from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Process(Base):
    pid = Column(Integer, primary_key=True, index=True)
    id = Column(String, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    keywords = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="processes")
