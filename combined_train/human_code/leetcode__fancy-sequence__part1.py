v1 = 10 ** 9 + 7

class C1(object):

    def __init__(self):
        self.__arr = []
        self.__ops = [[1, 0]]

    def append(self, a1):
        """
        """
        self.__arr.append(a1)
        self.__ops.append(self.__ops[-1][:])

    def addAll(self, a1):
        """
        """
        self.__ops[-1][1] = (self.__ops[-1][1] + a1) % v1

    def multAll(self, a1):
        """
        """
        self.__ops[-1] = [self.__ops[-1][0] * a1 % v1, self.__ops[-1][1] * a1 % v1]

    def getIndex(self, a1):
        """
        """
        if a1 >= len(self.__arr):
            return -1
        v1, v2 = self.__ops[a1]
        v3, v4 = self.__ops[-1]
        v5 = v3 * pow(v1, v1 - 2, v1) % v1
        v6 = (v4 - v2 * v5) % v1
        return (self.__arr[a1] * v5 + v6) % v1
