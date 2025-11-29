import threading

class C1:

    def __init__(self):
        self._condition = threading.Condition()
        self._pending_h = 0

    def hydrogen(self, a1):
        with self._condition:
            while self._pending_h == 2:
                self._condition.wait()
            self._pending_h += 1
            a1()
            if self._pending_h == 2:
                self._condition.notify()

    def oxygen(self, a1):
        with self._condition:
            while self._pending_h < 2:
                self._condition.wait()
            self._pending_h -= 2
            a1()
            self._condition.notify()
            self._condition.notify()
