from timer import Timer
from pynput import keyboard
import logging


class Shortcuts:
    
    def __init__(self, q_shortcuts, q_start_time):
        self.timer = Timer()
        self.keyboard_controller = keyboard.Controller()
        
        self.q_shortcut = q_shortcuts
        self.q_start_time = q_start_time

    def start_timer(self):
        self.timer.start_timer()
        self.q_shortcut.push(0)
        logging.debug('Timer started at {}'.format(self.timer.get_start_time()))
    
    def reset_timer(self):
        self.timer.stop_timer()
        self.q_shortcut.push(1)
        logging.debug('Timer stopped')

    def get_timestamp(self):
        self.sync_with_ui_timer()
    
        # start timer if it wasn't
        if self.timer.get_start_time() is None:
            self.start_timer()
            return
    
        timestamp = self.timer.get_timestamp_str()
        self.keyboard_controller.type("{}    ".format(timestamp))

    def sync_with_ui_timer(self):
        while not self.q_start_time.empty():
            self.timer.set_start_time(self.q_start_time.pop())

    def start(self):
        with keyboard.GlobalHotKeys({
                '<cmd>+<shift>+r': self.reset_timer,
                '<ctrl>+<enter>': self.get_timestamp}) as h:
            h.join()