import threading

class C1:

    def __init__(self, a1):
        self.n = a1
        self.state = 0
        self.next_number = 1
        self.condition = threading.Condition()

    def zero(self, a1):
        for v1 in range(self.n):
            with self.condition:
                while self.state != 0:
                    self.condition.wait()
                a1(0)
                self.state = 1 if self.next_number % 2 == 1 else 2
                self.condition.notifyAll()

    def even(self, a1):
        for v1 in range(2, self.n + 1, 2):
            with self.condition:
                while self.state != 2:
                    self.condition.wait()
                a1(v1)
                self.next_number += 1
                self.state = 0
                self.condition.notifyAll()

    def odd(self, a1):
        for v1 in range(1, self.n + 1, 2):
            with self.condition:
                while self.state != 1:
                    self.condition.wait()
                a1(v1)
                self.next_number += 1
                self.state = 0
                self.condition.notifyAll()
