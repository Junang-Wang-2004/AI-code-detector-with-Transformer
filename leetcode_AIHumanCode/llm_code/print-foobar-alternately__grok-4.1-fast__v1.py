import threading

class FooBar:
    def __init__(self, n):
        self.total = n
        self.foo_turn = threading.Semaphore(1)
        self.bar_turn = threading.Semaphore(0)

    def foo(self, printFoo):
        for _ in range(self.total):
            self.foo_turn.acquire()
            printFoo()
            self.bar_turn.release()

    def bar(self, printBar):
        for _ in range(self.total):
            self.bar_turn.acquire()
            printBar()
            self.foo_turn.release()
