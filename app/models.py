import enum
from sqlalchemy import Column, Integer, String, Enum, DateTime, Date, func
from .database import Base

class PriorityEnum(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

class StatusEnum(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(StatusEnum), default=StatusEnum.pending)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.medium)
    created_at = Column(DateTime, server_default=func.now())
    due_date = Column(Date, nullable=True)
