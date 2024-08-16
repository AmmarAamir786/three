from sqlmodel import Session, select
from app.models.notification_models import Notification, NotificationCreate

def create_notification(session: Session, notification: NotificationCreate) -> Notification:
    db_notification = Notification.from_orm(notification)
    session.add(db_notification)
    session.commit()
    session.refresh(db_notification)
    return db_notification

def get_notification(session: Session, notification_id: int) -> Notification:
    statement = select(Notification).where(Notification.id == notification_id)
    return session.exec(statement).first()

def get_notifications(session: Session, skip: int = 0, limit: int = 10) -> list[Notification]:
    statement = select(Notification).offset(skip).limit(limit)
    return session.exec(statement).all()
