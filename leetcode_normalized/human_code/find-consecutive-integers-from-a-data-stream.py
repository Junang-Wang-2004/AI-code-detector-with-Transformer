class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__value = a1
        self.__k = a2
        self.__cnt = 0

    def consec(self, a1):
        """
        """
        if a1 == self.__value:
            self.__cnt += 1
        else:
            self.__cnt = 0
        return self.__cnt >= self.__k
