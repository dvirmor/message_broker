# send.py
import pika
from datetime import datetime
import time

# Connection setup to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue='time_queue')

# Number of messages to send
num_messages = 10

for i in range(num_messages):
    # Get the current time
    current_time = datetime.now().isoformat()

    # Send the message
    channel.basic_publish(exchange='',
                          routing_key='time_queue',
                          body=current_time)
    
    print(f"[x] Sent {i+1}/{num_messages}: {current_time}")
    
    # Delay between messages
    time.sleep(1)

# Close the connection
connection.close()

