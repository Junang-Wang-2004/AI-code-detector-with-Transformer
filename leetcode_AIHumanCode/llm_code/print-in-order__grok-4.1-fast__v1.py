import threading


class Foo:
    def __init__(self):
        self.ready1 = threading.Event()
        self.ready2 = threading.Event()

    def first(self, printFirst):
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.ready1.set()

    def second(self, printSecond):
        # printSecond() outputs "second". Do not change or remove this line.
        self.ready1.wait()
        printSecond()
        self.ready2.set()

    def third(self, printThird):
        # printThird() outputs "third". Do not change or remove this line.
        self.ready2.wait()
        printThird()
