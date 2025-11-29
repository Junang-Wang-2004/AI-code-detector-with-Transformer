import threading

class C1(object):

    def __init__(self):
        self.__cv = threading.Condition()
        self.__has_first = False
        self.__has_second = False

    def first(self, a1):
        """
        """
        with self.__cv:
            a1()
            self.__has_first = True
            self.__cv.notifyAll()

    def second(self, a1):
        """
        """
        with self.__cv:
            while not self.__has_first:
                self.__cv.wait()
            a1()
            self.__has_second = True
            self.__cv.notifyAll()

    def third(self, a1):
        """
        """
        with self.__cv:
            while not self.__has_second:
                self.__cv.wait()
            a1()
            self.__cv.notifyAll()
