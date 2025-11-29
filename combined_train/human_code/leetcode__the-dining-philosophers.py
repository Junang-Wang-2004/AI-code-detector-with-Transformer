import threading

class C1(object):

    def __init__(self):
        self._l = [threading.Lock() for v1 in range(5)]

    def wantsToEat(self, a1, a2, a3, a4, a5, a6):
        """
        """
        v1, v2 = (a1, (a1 + 4) % 5)
        v3, v4 = (v1, v2)
        if a1 % 2 == 0:
            v3, v4 = (v1, v2)
        else:
            v3, v4 = (v2, v1)
        with self._l[v3]:
            with self._l[v4]:
                a2()
                a3()
                a4()
                a5()
                a6()
