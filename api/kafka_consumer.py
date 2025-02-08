from confluent_kafka import Consumer
import psycopg2
import json

# Kafka Configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'traffic_consumer_group',
    'auto.offset.reset': 'earliest'
}

# PostgreSQL Configuration
conn = psycopg2.connect("dbname=logistics user=postgres password=postgres host=localhost")
cur = conn.cursor()

def process_traffic_data(data):
    print("Received data:", data)  # Debugging: Print the received data
    try:
        # Extract fields from the data
        segment_id = data.get('segment_id')
        speed_kmh = data.get('speed_kmh')
        coordinates = data.get('coordinates')

        if not all([segment_id, speed_kmh, coordinates]):
            print("Error: Missing required fields in data")
            return

        # Insert or update the database
        cur.execute("""
            INSERT INTO realtime_traffic (segment_id, speed_kmh, coordinates)
            VALUES (%s, %s, ST_SetSRID(ST_MakeLine(
                ST_MakePoint(%s, %s),
                ST_MakePoint(%s, %s)
            ), 4326))
            ON CONFLICT (segment_id) DO UPDATE
            SET speed_kmh = EXCLUDED.speed_kmh,
                coordinates = EXCLUDED.coordinates,
                timestamp = CURRENT_TIMESTAMP
        """, (
            segment_id,
            speed_kmh,
            coordinates[0][0], coordinates[0][1],  # First coordinate (longitude, latitude)
            coordinates[1][0], coordinates[1][1]   # Second coordinate (longitude, latitude)
        ))
        conn.commit()
        print("Data successfully processed and stored in the database.")
    except Exception as e:
        print(f"Error processing data: {e}")

consumer = Consumer(conf)
consumer.subscribe(['traffic_updates'])

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print(f"Error: {msg.error()}")
        continue
    try:
        data = json.loads(msg.value())
        process_traffic_data(data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")