from queue import Empty, Queue

from kafka.consumer.fetcher import ConsumerRecord

from .stoppable_thread import StoppableThread


class MessageProcessingThread(StoppableThread):

    def __init__(self, messages_queue: Queue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__messages_queue = messages_queue

    def run(self):
        while not self.is_stopped():
            try:
                _: ConsumerRecord = self.__messages_queue.get(timeout=1)
            except Empty:
                ...
