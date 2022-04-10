import queue


class SingleQueue:
    def __init__(self):
        self.queue = queue.Queue(maxsize=1)

    def push(self, value):
        if not self.empty():
            self.queue.get_nowait()
        self.queue.put_nowait(value)

    def pop(self):
        return self.queue.get_nowait()

    def empty(self):
        return self.queue.qsize() == 0
