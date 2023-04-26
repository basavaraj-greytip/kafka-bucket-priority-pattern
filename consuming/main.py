import logging
from queue import Queue
from time import sleep

from config import RUN_SECONDS, TOPIC_NAME, WORKERS_NUM
from src import ConsumerThread, MessageProcessingThread


def main():
    message_queue = Queue()

    message_processor = MessageProcessingThread(messages_queue=message_queue)
    message_consumers = [
        ConsumerThread(
            message_queue=message_queue,
            name=f'consumer-{TOPIC_NAME}-{i + 1:0>4}'.ljust(20, ' '),
        )
        for i in range(WORKERS_NUM)
    ]

    threads = [message_processor] + message_consumers

    for t in threads:
        t.start()

    sleep(RUN_SECONDS)

    for t in threads:
        t.stop()

    for t in threads:
        t.join()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
    logging.getLogger('kafka').setLevel(logging.WARNING)
    main()
