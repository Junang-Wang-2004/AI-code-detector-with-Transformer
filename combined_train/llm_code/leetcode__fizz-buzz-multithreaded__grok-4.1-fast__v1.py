import threading

class C1:

    def __init__(self, a1):
        self.maxn = a1
        self.status = 0
        self.sync = threading.Condition()

    def _step(self, a1, a2, a3):
        for v1 in range(1, self.maxn + 1):
            with self.sync:
                while self.status != a1:
                    self.sync.wait()
                self.status = (self.status + 1) % 4
                if a2(v1):
                    a3()
                self.sync.notify_all()

    def fizz(self, a1):
        """
        """
        self._step(0, lambda x: x % 3 == 0 and x % 5 != 0, a1)

    def buzz(self, a1):
        """
        """
        self._step(1, lambda x: x % 5 == 0 and x % 3 != 0, a1)

    def fizzbuzz(self, a1):
        """
        """
        self._step(2, lambda x: x % 3 == 0 and x % 5 == 0, a1)

    def number(self, a1):
        """
        """
        self._step(3, lambda x: x % 3 != 0 and x % 5 != 0, a1)
