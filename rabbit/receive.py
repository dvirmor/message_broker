# receive.py
import pika
from datetime import datetime
import matplotlib.pyplot as plt

# Connection setup to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue='time_queue')

# To store time differences
time_diffs = []
message_count = 10  # Should match the number of messages sent
received_count = 0

def callback(ch, method, properties, body):
    global received_count
    # Receive message and calculate time difference
    sent_time = datetime.fromisoformat(body.decode())
    received_time = datetime.now()
    time_diff = (received_time - sent_time).total_seconds()
    
    # Store time difference
    time_diffs.append(time_diff)
    received_count += 1
    
    print(f"[x] Received {received_count}/{message_count}: {sent_time}")
    print(f"Time difference: {time_diff} seconds")
    
    # If all messages are received, plot the graph
    if received_count == message_count:
        plot_time_diffs(time_diffs)

def plot_time_diffs(time_diffs):
    # Plot time differences
    plt.plot(range(1, message_count + 1), time_diffs, marker='o')
    plt.title('Time Difference Between Sending and Receiving Messages')
    plt.xlabel('Message Number')
    plt.ylabel('Time Difference (seconds)')
    plt.grid(True)
    plt.show()

# Set up subscription on the queue
channel.basic_consume(queue='time_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

