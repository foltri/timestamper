import threading
from single_queue import SingleQueue
from statusbar import StatusBar
from shortcuts import Shortcuts
import logging

logging.basicConfig(level=logging.WARNING)


class TimestamperApp:

    def __init__(self):
        self.q_shortcut = SingleQueue()
        self.q_start_time = SingleQueue()

    def run(self):
        threading.Thread(target=Shortcuts(self.q_shortcut, self.q_start_time).start, daemon=True).start()
        StatusBar(self.q_shortcut, self.q_start_time).run()


if __name__ == '__main__':
    TimestamperApp().run()
