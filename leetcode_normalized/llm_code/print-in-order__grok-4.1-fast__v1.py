import threading

class C1:

    def __init__(self):
        self.ready1 = threading.Event()
        self.ready2 = threading.Event()

    def first(self, a1):
        a1()
        self.ready1.set()

    def second(self, a1):
        self.ready1.wait()
        a1()
        self.ready2.set()

    def third(self, a1):
        self.ready2.wait()
        a1()
