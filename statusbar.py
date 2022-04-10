# -*- coding: utf-8 -*-

import rumps
from timer import Timer
import logging
import os


class StatusBar(rumps.App):
    NAME = "timestamper"

    SETTINGS = "settings.json"
    DEF_SETTING = {
        "enter": True,
        "tab": True
    }

    def __init__(self, q_shortcut, q_start_time):
        super(StatusBar, self).__init__(self.NAME)
        self.SETTINGS_PATH = os.path.join(self._application_support, self.SETTINGS)

        self.quit_button = "quit"
        self.menu = ["start timer - ^⏎", "reset timer - ⌘⇧R"]
        self.menu.insert_after("reset timer - ⌘⇧R", rumps.MenuItem("paste timestamp - ^⏎"))

        self.timer = Timer()
        self.q_shortcut = q_shortcut
        self.q_start_time = q_start_time

        # timer to update app title with time when timer is on
        self.title_updater = rumps.Timer(self.update_title, 1)

    @rumps.clicked("start timer - ^⏎")
    def start(self, sender):
        self.timer.start_timer()
        self.title_updater.start()
        self.update_shortcut_timer()

    @rumps.clicked("reset timer - ⌘⇧R")
    def stop(self, sender):
        self.title = self.NAME
        self.timer.stop_timer()
        self.title_updater.stop()
        self.update_shortcut_timer()

    def update_title(self, sender):
        self.title = self.timer.get_timestamp_str()

    def update_shortcut_timer(self):
        self.q_start_time.push(self.timer.get_start_time())

    @rumps.timer(1)
    def shortcut_handler(self, sender):
        logging.debug("tick")
        while not self.q_shortcut.empty():
            cmd = self.q_shortcut.pop()
            if cmd == 0:
                self.start(None)
            elif cmd == 1:
                self.stop(None)
