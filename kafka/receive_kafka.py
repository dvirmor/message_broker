# receive_kafka.py
from kafka import KafkaConsumer
from datetime import datetime
import matplotlib.pyplot as plt

# Create Kafka consumer
consumer = KafkaConsumer(
    'time_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='time-group'
)

# To store time differences
time_diffs = []
message_count = 10  # Should match the number of messages sent
received_count = 0

def calculate_time_diff(message):
    global received_count
    # Receive message and calculate time difference
    sent_time = datetime.fromisoformat(message.decode())
    received_time = datetime.now()
    time_diff = (received_time - sent_time).total_seconds()
    
    # Store time difference
    time_diffs.append(time_diff)
    received_count += 1
    
    print(f"[x] Received {received_count}/{message_count}: {sent_time}")
    print(f"Time difference: {time_diff} seconds")

def plot_time_diffs():
    # Plot time differences
    plt.plot(range(1, message_count + 1), time_diffs, marker='o')
    plt.title('Time Difference Between Sending and Receiving Messages (Kafka)')
    plt.xlabel('Message Number')
    plt.ylabel('Time Difference (seconds)')
    plt.grid(True)
    plt.show()

# Consume messages from Kafka topic
for message in consumer:
    calculate_time_diff(message.value)

    # Once all messages are received, plot the graph
    if received_count == message_count:
        plot_time_diffs()
        break


