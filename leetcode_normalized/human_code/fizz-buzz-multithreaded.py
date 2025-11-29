import threading

class C1(object):

    def __init__(self, a1):
        self.__n = a1
        self.__curr = 0
        self.__cv = threading.Condition()

    def fizz(self, a1):
        """
        """
        for v1 in range(1, self.__n + 1):
            with self.__cv:
                while self.__curr % 4 != 0:
                    self.__cv.wait()
                self.__curr += 1
                if v1 % 3 == 0 and v1 % 5 != 0:
                    a1()
                self.__cv.notify_all()

    def buzz(self, a1):
        """
        """
        for v1 in range(1, self.__n + 1):
            with self.__cv:
                while self.__curr % 4 != 1:
                    self.__cv.wait()
                self.__curr += 1
                if v1 % 3 != 0 and v1 % 5 == 0:
                    a1()
                self.__cv.notify_all()

    def fizzbuzz(self, a1):
        """
        """
        for v1 in range(1, self.__n + 1):
            with self.__cv:
                while self.__curr % 4 != 2:
                    self.__cv.wait()
                self.__curr += 1
                if v1 % 3 == 0 and v1 % 5 == 0:
                    a1()
                self.__cv.notify_all()

    def number(self, a1):
        """
        """
        for v1 in range(1, self.__n + 1):
            with self.__cv:
                while self.__curr % 4 != 3:
                    self.__cv.wait()
                self.__curr += 1
                if v1 % 3 != 0 and v1 % 5 != 0:
                    a1(v1)
                self.__cv.notify_all()
