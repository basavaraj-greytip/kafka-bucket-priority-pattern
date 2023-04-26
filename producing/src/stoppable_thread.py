from threading import Event, Thread


class StoppableThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__stop_event = Event()

    def stop(self):
        self.__stop_event.set()

    def is_stopped(self) -> bool:
        return self.__stop_event.is_set()

    def run(self):
        while not self.is_stopped():
            ...
