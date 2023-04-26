import logging
from queue import Queue
from time import sleep

from config import RUN_SECONDS, TOPIC_NAME, WORKERS_NUM
from src import MessageCreatingThread, ProducerThread, StoppableThread


def main():
    queue = Queue()

    creator = MessageCreatingThread(messages_queue=queue)
    producers: list[StoppableThread] = [
        ProducerThread(
            messages_queue=queue,
            name=f'producer-{TOPIC_NAME}-{i + 1:0>4}'.ljust(20, ' '),
        )
        for i in range(WORKERS_NUM)
    ]

    threads = [creator] + producers

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
