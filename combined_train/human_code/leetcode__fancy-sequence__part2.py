class C1(object):

    def __init__(self):
        self.__arr = []
        self.__op = [1, 0]

    def append(self, a1):
        """
        """
        self.__arr.append((a1 - self.__op[1]) * pow(self.__op[0], MOD - 2, MOD) % MOD)

    def addAll(self, a1):
        """
        """
        self.__op[1] = (self.__op[1] + a1) % MOD

    def multAll(self, a1):
        """
        """
        self.__op = [self.__op[0] * a1 % MOD, self.__op[1] * a1 % MOD]

    def getIndex(self, a1):
        """
        """
        if a1 >= len(self.__arr):
            return -1
        v1, v2 = self.__op
        return (self.__arr[a1] * v1 + v2) % MOD
