import json
import logging
from queue import Queue
from random import uniform
from time import sleep

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord
from kafka.structs import TopicPartition

from config import (
    CONSUMER_MIN_SLEEP_TIME,
    CONSUMER_MAX_SLEEP_TIME,
    BOOTSTRAP_SERVERS,
    TOPIC_NAME
)
from .stoppable_thread import StoppableThread


class ConsumerThread(StoppableThread):

    def __init__(self, message_queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__messages_queue = message_queue
        self.__logger = logging.getLogger(self.name)

    def run(self):
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            group_id=f'{TOPIC_NAME}__consumers',
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        )

        while not self.is_stopped():
            records: dict[TopicPartition, list[ConsumerRecord]] = consumer.poll(60, max_records=1)

            for partition, messages in records.items():
                for message in messages:
                    self.__logger.info(f'Consumed message: {message.value}')
                    self.__messages_queue.put(message)

            sleep(uniform(CONSUMER_MIN_SLEEP_TIME, CONSUMER_MAX_SLEEP_TIME))

        consumer.close()
