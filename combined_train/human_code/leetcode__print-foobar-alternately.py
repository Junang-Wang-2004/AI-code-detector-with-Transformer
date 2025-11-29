import threading

class C1(object):

    def __init__(self, a1):
        self.__n = a1
        self.__curr = False
        self.__cv = threading.Condition()

    def foo(self, a1):
        """
        """
        for v1 in range(self.__n):
            with self.__cv:
                while self.__curr != False:
                    self.__cv.wait()
                self.__curr = not self.__curr
                a1()
                self.__cv.notify()

    def bar(self, a1):
        """
        """
        for v1 in range(self.__n):
            with self.__cv:
                while self.__curr != True:
                    self.__cv.wait()
                self.__curr = not self.__curr
                a1()
                self.__cv.notify()
