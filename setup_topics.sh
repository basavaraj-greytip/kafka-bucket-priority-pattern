#!/bin/bash

export $(xargs < .env)

echo "Recreating topic $LOW_TOPIC_NAME with $LOW_TOPIC_PARTITIONS partitions."

# Delete old low topic
docker exec kafka-1 kafka-topics \
  --bootstrap-server localhost:9092 \
  --if-exists \
  --delete \
  --topic "$LOW_TOPIC_NAME"

# Create low topic
docker exec kafka-1 kafka-topics \
  --create \
  --if-not-exists \
  --bootstrap-server localhost:9092 \
  --partitions "$LOW_TOPIC_PARTITIONS" \
  --replication-factor "$TOPIC_REPLICATION_FACTOR" \
  --topic "$LOW_TOPIC_NAME"

echo "Recreating topic $MEDIUM_TOPIC_NAME with $MEDIUM_TOPIC_PARTITIONS partitions."

# Delete old medium topic
docker exec kafka-1 kafka-topics \
  --bootstrap-server localhost:9092 \
  --if-exists \
  --delete \
  --topic "$MEDIUM_TOPIC_NAME"

# Create medium topic
docker exec kafka-1 kafka-topics \
  --create \
  --if-not-exists \
  --bootstrap-server localhost:9092 \
  --partitions "$MEDIUM_TOPIC_PARTITIONS" \
  --replication-factor "$TOPIC_REPLICATION_FACTOR" \
  --topic "$MEDIUM_TOPIC_NAME"

echo "Recreating topic $HIGH_TOPIC_NAME with $HIGH_TOPIC_PARTITIONS partitions."

# Delete old high topic
docker exec kafka-1 kafka-topics \
  --bootstrap-server localhost:9092 \
  --if-exists \
  --delete \
  --topic "$HIGH_TOPIC_NAME"

# Create high topic
docker exec kafka-1 kafka-topics \
  --create \
  --if-not-exists \
  --bootstrap-server localhost:9092 \
  --partitions "$HIGH_TOPIC_PARTITIONS" \
  --replication-factor "$TOPIC_REPLICATION_FACTOR" \
  --topic "$HIGH_TOPIC_NAME"
