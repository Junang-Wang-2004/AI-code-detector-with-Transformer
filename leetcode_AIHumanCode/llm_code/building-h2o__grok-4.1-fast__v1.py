import threading


class H2O:
    def __init__(self):
        self._condition = threading.Condition()
        self._pending_h = 0

    def hydrogen(self, releaseHydrogen):
        with self._condition:
            while self._pending_h == 2:
                self._condition.wait()
            self._pending_h += 1
            releaseHydrogen()
            if self._pending_h == 2:
                self._condition.notify()

    def oxygen(self, releaseOxygen):
        with self._condition:
            while self._pending_h < 2:
                self._condition.wait()
            self._pending_h -= 2
            releaseOxygen()
            self._condition.notify()
            self._condition.notify()
