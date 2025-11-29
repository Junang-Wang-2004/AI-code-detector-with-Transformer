class C1(object):

    def __init__(self, a1):
        """
        """
        self.__A = a1
        self.__i = 0
        self.__cnt = 0

    def next(self, a1):
        """
        """
        while self.__i < len(self.__A):
            if a1 > self.__A[self.__i] - self.__cnt:
                a1 -= self.__A[self.__i] - self.__cnt
                self.__cnt = 0
                self.__i += 2
            else:
                self.__cnt += a1
                return self.__A[self.__i + 1]
        return -1
