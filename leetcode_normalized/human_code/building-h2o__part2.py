class C1(object):

    def __init__(self):
        self.__nH = 0
        self.__nO = 0
        self.__cv = threading.Condition()

    def hydrogen(self, a1):
        """
        """
        with self.__cv:
            while self.__nH + 1 - 2 * self.__nO > 2:
                self.__cv.wait()
            self.__nH += 1
            a1()
            self.__cv.notifyAll()

    def oxygen(self, a1):
        """
        """
        with self.__cv:
            while 2 * (self.__nO + 1) - self.__nH > 2:
                self.__cv.wait()
            self.__nO += 1
            a1()
            self.__cv.notifyAll()
