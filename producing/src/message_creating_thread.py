from queue import Queue
from random import uniform
from time import sleep
from uuid import uuid4

from config import CREATOR_MIN_SLEEP_TIME, CREATOR_MAX_SLEEP_TIME
from .stoppable_thread import StoppableThread


class MessageCreatingThread(StoppableThread):

    def __init__(self, messages_queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__messages_queue = messages_queue

    def run(self):
        while not self.is_stopped():
            self.__messages_queue.put(self.create_message())

    @staticmethod
    def create_message() -> dict:
        # Simulates real-time message creating
        sleep(uniform(CREATOR_MIN_SLEEP_TIME, CREATOR_MAX_SLEEP_TIME))

        return {
            'uuid': str(uuid4()),
        }
