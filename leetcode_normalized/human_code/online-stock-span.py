class C1(object):

    def __init__(self):
        self.__s = []

    def next(self, a1):
        """
        """
        v1 = 1
        while self.__s and self.__s[-1][0] <= a1:
            v1 += self.__s.pop()[1]
        self.__s.append([a1, v1])
        return v1
