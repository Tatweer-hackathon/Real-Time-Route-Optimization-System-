from confluent_kafka import Producer
import requests
import json
import time

# Kafka configuration
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

# TomTom API configuration
TOMTOM_API_KEY ='C1CltC7X8EMuIYK6tQfO0FFDGUqIfFvI' 
TOMTOM_API_URL = "https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json"


# Kafka Configuration
conf = {'bootstrap.servers': 'localhost:9092'}
producer = Producer(conf)

def fetch_traffic_data(lat, lon):
    params = {
        'point': f'{lat},{lon}',
        'unit': 'KMPH',
        'key': TOMTOM_API_KEY
    }
    response = requests.get(TOMTOM_API_URL, params=params)
    return response.json() if response.status_code == 200 else None

def delivery_report(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()}')

def produce_traffic_data():
    # Example coordinates (update with your delivery points)
    locations = [
        (34.0195, -118.4912),  # Point A
        (34.0250, -118.5000),  # Point B
        (34.0300, -118.5100)   # Point C
    ]
    while True:
        for lat, lon in locations:
            data = fetch_traffic_data(lat, lon)
            print(data)
            print('')
            if data:
                producer.produce(
                    'traffic_updates',
                    json.dumps(data),
                    callback=delivery_report
                )
                producer.flush()
        time.sleep(300)  # Fetch data every 5 minutes

if __name__ == '__main__':
    produce_traffic_data()