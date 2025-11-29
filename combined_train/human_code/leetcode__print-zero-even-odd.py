import threading

class C1(object):

    def __init__(self, a1):
        self.__n = a1
        self.__curr = 0
        self.__cv = threading.Condition()

    def zero(self, a1):
        """
        """
        for v1 in range(self.__n):
            with self.__cv:
                while self.__curr % 2 != 0:
                    self.__cv.wait()
                self.__curr += 1
                a1(0)
                self.__cv.notifyAll()

    def even(self, a1):
        """
        """
        for v1 in range(2, self.__n + 1, 2):
            with self.__cv:
                while self.__curr % 4 != 3:
                    self.__cv.wait()
                self.__curr += 1
                a1(v1)
                self.__cv.notifyAll()

    def odd(self, a1):
        """
        """
        for v1 in range(1, self.__n + 1, 2):
            with self.__cv:
                while self.__curr % 4 != 1:
                    self.__cv.wait()
                self.__curr += 1
                a1(v1)
                self.__cv.notifyAll()
