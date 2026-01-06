# timer.py

import threading
import sys
import time

class TurnTimer:
    def __init__(self, seconds: int):
        self.seconds = seconds
        self.time_up = False

    def _countdown(self):
        time.sleep(self.seconds)
        self.time_up = True
        print("\n⏰ Time's up! You took too long.")
        sys.exit(0)

    def start(self):
        timer_thread = threading.Thread(target=self._countdown, daemon=True)
        timer_thread.start()
