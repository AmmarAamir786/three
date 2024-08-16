# # app/deps.py
# from kafka import KafkaProducer
# from app.settings import settings

# producer = KafkaProducer(bootstrap_servers=settings.KAFKA_SERVER)

# def get_kafka_producer():
#     return producer


from aiokafka import AIOKafkaProducer
from sqlmodel import Session
from app.db_engine import engine

# Kafka Producer as a dependency
async def get_kafka_producer():
    producer = AIOKafkaProducer(bootstrap_servers='broker:19092')
    await producer.start()
    try:
        yield producer
    finally:
        await producer.stop()

def get_session():
    with Session(engine) as session:
        yield session
