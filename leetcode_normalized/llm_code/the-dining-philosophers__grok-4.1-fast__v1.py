import threading

class C1:

    def __init__(self):
        self.fork_locks = [threading.Lock() for v1 in range(5)]

    def wantsToEat(self, a1, a2, a3, a4, a5, a6):
        v1 = a1
        v2 = (a1 + 4) % 5
        v3 = min(v1, v2)
        v4 = max(v1, v2)
        with self.fork_locks[v3]:
            with self.fork_locks[v4]:
                a2()
                a3()
                a4()
                a5()
                a6()
