# send_kafka.py
from kafka import KafkaProducer
from datetime import datetime
import time

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Topic name
topic_name = 'time_topic'

# Number of messages to send
num_messages = 10

for i in range(num_messages):
    # Get the current time
    current_time = datetime.now().isoformat().encode('utf-8')

    # Send the message
    producer.send(topic_name, current_time)
    
    print(f"[x] Sent {i+1}/{num_messages}: {current_time.decode()}")

    # Delay between messages
    time.sleep(1)

# Close the producer connection
producer.flush()
producer.close()

