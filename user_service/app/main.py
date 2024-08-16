# app/main.py
from fastapi import FastAPI, Depends
from app.models.user_model import User
from app.crud.user_crud import get_user, create_user
from app.deps import get_kafka_producer
from kafka import KafkaProducer
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from user_service.app import settings
from app.deps import get_session, get_kafka_producer


app = FastAPI()

@app.post("/users/", response_model=User)
def create_new_user(user: User, producer: KafkaProducer = Depends(get_kafka_producer)):
    new_user = create_user(user)
    producer.send(settings.KAFKA_TOPIC, key=b"user_created", value=user.json().encode('utf-8'))
    return new_user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    user = get_user(user_id)
    return user
