import threading

class C1(object):

    def __init__(self):
        self.__l = threading.Lock()
        self.__light = 1

    def carArrived(self, a1, a2, a3, a4, a5):
        """
        """
        with self.__l:
            if self.__light != a2:
                self.__light = a2
                a4()
            a5()
