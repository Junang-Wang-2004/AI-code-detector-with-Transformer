import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.state = 0
        self.next_number = 1
        self.condition = threading.Condition()

    def zero(self, printNumber):
        for _ in range(self.n):
            with self.condition:
                while self.state != 0:
                    self.condition.wait()
                printNumber(0)
                self.state = 1 if self.next_number % 2 == 1 else 2
                self.condition.notifyAll()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            with self.condition:
                while self.state != 2:
                    self.condition.wait()
                printNumber(i)
                self.next_number += 1
                self.state = 0
                self.condition.notifyAll()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            with self.condition:
                while self.state != 1:
                    self.condition.wait()
                printNumber(i)
                self.next_number += 1
                self.state = 0
                self.condition.notifyAll()
