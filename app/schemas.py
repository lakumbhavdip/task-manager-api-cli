from pydantic import BaseModel, Field
from datetime import datetime, date
from typing import Optional
from .models import StatusEnum, PriorityEnum

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    priority: PriorityEnum = PriorityEnum.medium
    due_date: Optional[date] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    due_date: Optional[date] = None

class Task(TaskBase):
    id: int
    status: StatusEnum
    created_at: datetime

    class Config:
        from_attributes = True
