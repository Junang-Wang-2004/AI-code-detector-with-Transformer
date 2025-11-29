import threading

class C1:

    def __init__(self, a1):
        self.total = a1
        self.foo_turn = threading.Semaphore(1)
        self.bar_turn = threading.Semaphore(0)

    def foo(self, a1):
        for v1 in range(self.total):
            self.foo_turn.acquire()
            a1()
            self.bar_turn.release()

    def bar(self, a1):
        for v1 in range(self.total):
            self.bar_turn.acquire()
            a1()
            self.foo_turn.release()
