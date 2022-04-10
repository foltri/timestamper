import datetime
import logging


class Timer:

    def __init__(self):
        # time of starting the timer
        self._start_time = None

    def start_timer(self):
        self._start_time = datetime.datetime.now()

    def set_start_time(self, datetime_value):
        self._start_time = datetime_value

    def get_start_time(self):
        return self._start_time

    def stop_timer(self):
        self._start_time = None

    def get_timestamp_str(self):
        if self._start_time is None:
            logging.warning("The timer is stopped")
            return 0
        else:
            timestamp = "{:02}:{:02}:{:02}".format(
                int((datetime.datetime.now() - self._start_time).total_seconds() // 3600),
                int((datetime.datetime.now() - self._start_time).total_seconds() % 3600) // 60,
                int((datetime.datetime.now() - self._start_time).total_seconds() % 60))

            return timestamp


if __name__ == '__main__':
    import time

    t = Timer()
    t.start_timer()

    for i in range(5):
        time.sleep(1)
        print(t.get_timestamp_str())

    t.stop_timer()
    t.get_timestamp_str()

    t.start_timer()
    t._start_time -= datetime.timedelta(minutes=30, seconds=58)

    for i in range(5):
        time.sleep(1)
        print(t.get_timestamp_str())
