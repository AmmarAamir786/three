
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class NotificationBase(SQLModel):
    title: str
    message: str
    recipient: str
    sent_at: Optional[datetime] = None

class Notification(NotificationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class NotificationCreate(NotificationBase):
    pass
