from fastapi import FastAPI, Depends
from app.crud.notification_crud import create_notification, get_notification, get_notifications
from app.models.notification_models import Notification, NotificationCreate
from sqlmodel import Session
from app.deps import get_session
# from kafka import KafkaProducer 
from aiokafka import AIOKafkaProducer
from app.notification_service_pb2 import NotificationMessage
import app.db_engine as db

app = FastAPI()

producer =AIOKafkaProducer(bootstrap_servers='kafka:9092')

@app.on_event("startup")
def on_startup():
    db.init_db()

@app.post("/notifications/", response_model=Notification)
def create_new_notification(notification: NotificationCreate, session: Session = Depends(get_session)):
    created_notification = create_notification(session, notification)
    
    notification_message = NotificationMessage(
        id=created_notification.id,
        title=created_notification.title,
        message=created_notification.message,
        recipient=created_notification.recipient,
        sent_at=created_notification.sent_at.isoformat() if created_notification.sent_at else None
    )
    producer.send('notifications', notification_message.SerializeToString())
    
    return created_notification

@app.get("/notifications/{notification_id}", response_model=Notification)
def read_notification(notification_id: int, session: Session = Depends(get_session)):
    return get_notification(session, notification_id)

@app.get("/notifications/", response_model=list[Notification])
def read_notifications(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    return get_notifications(session, skip=skip, limit=limit)


