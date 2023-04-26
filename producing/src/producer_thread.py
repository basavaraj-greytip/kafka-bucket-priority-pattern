import json
import logging
from queue import Queue, Empty

from kafka import KafkaProducer

from config import BOOTSTRAP_SERVERS, TOPIC_NAME
from .stoppable_thread import StoppableThread


class ProducerThread(StoppableThread):
    def __init__(self, messages_queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__messages_queue = messages_queue
        self.__logger = logging.getLogger(self.name)

    def run(self):
        producer = KafkaProducer(
            bootstrap_servers=BOOTSTRAP_SERVERS,
            value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        )

        while not self.is_stopped():
            try:
                message = self.__messages_queue.get(timeout=1)
            except Empty:
                ...
            else:
                producer.send(TOPIC_NAME, message)
                self.__logger.info(f'Produced message: {message}')

        producer.flush()
