import time
import json
import random
from kafka import KafkaProducer

def generate_sensor_data():
    return {
        "sensor_id": random.randint(1, 5),
        "temperature": round(random.uniform(20, 35), 2),
        "humidity": round(random.uniform(30, 80), 2),
        "timestamp": int(time.time())
    }

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = generate_sensor_data()
    producer.send('sensor_data', value=data)
    print(f"Enviado: {data}")
    time.sleep(1)