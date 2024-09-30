# Message Broker

## Rabbit
### Setup Rabbit Environemnt
#### Start a Rabbit Server
```bash
docker run -it --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```
### Run the sender and the receiver
1. Run the receiver script receive.py to start waiting for messages:
   ```bash
   python3 recieve.py
   ```
2. Run the sender script send.py to send 10 messages:
   ```bash
   python3 send.py
   ```

## Kafka
### Setup Kafka Environemnt
#### Start a Kafka broker
```bash
docker run -d -p 9092:9092 --name broker apache/kafka:latest
```
#### Open a shell in the broker container
```bash
docker exec --workdir /opt/kafka/bin/ -it broker sh
```
#### Create a topic
```bash
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic time_topic
```
### Run the sender and the receiver
1. Run the receiver script receive_kafka.py to start waiting for messages:
   ```bash
   python3 recieve_kafka.py
   ```
2. Run the sender script send_kafka.py to send 10 messages:
   ```bash
   python3 send_kafka.py
   ```
