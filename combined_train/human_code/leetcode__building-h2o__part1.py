import threading

class C1(object):

    def __init__(self):
        self.__l = threading.Lock()
        self.__nH = 0
        self.__nO = 0
        self.__releaseHydrogen = None
        self.__releaseOxygen = None

    def hydrogen(self, a1):
        with self.__l:
            self.__releaseHydrogen = a1
            self.__nH += 1
            self.__output()

    def oxygen(self, a1):
        with self.__l:
            self.__releaseOxygen = a1
            self.__nO += 1
            self.__output()

    def __output(self):
        while self.__nH >= 2 and self.__nO >= 1:
            self.__nH -= 2
            self.__nO -= 1
            self.__releaseHydrogen()
            self.__releaseHydrogen()
            self.__releaseOxygen()
