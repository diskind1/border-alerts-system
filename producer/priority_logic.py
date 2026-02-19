import json
import uuid
from redis_connection import r_con
import os
from dotenv import load_dotenv
load_dotenv()

from confluent_kafka import Producer

from pydantic import BaseModel
from typing import List


r = r_con()


def get_producer() -> Producer:
    return Producer({"bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP", "kafka:9092")})

KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "Incoming-notifications")

class NotificationIn(BaseModel):
    border: str
    zone: str
    timestamp: str
    people_count: int
    weapons_count: int
    vehicle_type: str
    distance_from_fence_m: int
    visibility_quality: float


def upload_notifications(notification: List[NotificationIn]):
    producer = get_producer()

    for o in notification:
        doc = o.model_dump()
        doc["priority"] = "normal_queue"
        if doc["weapons_count"] > 0 or doc["distance_from_fence_m"] <= 50 or doc["people_count"] >= 8 or doc["vehicle_type"] == "truck":
            doc["priority"] = "urgent_queue"

        elif doc["distance_from_fence_m"] <= 150 and doc["people_count"] >= 4:
            doc["priority"] = "urgent_queue"

        elif doc["vehicle_type"] == "jeep" and doc["people_count"] >= 3:
            doc["priority"] = "urgent_queue"


        payload = {k: v for k, v in doc.items() if k != "_id"}
        producer.produce(
            topic=KAFKA_TOPIC,
            value=json.dumps(payload).encode("utf-8"),
        )

    producer.flush()
    # return {"topic": KAFKA_TOPIC}
