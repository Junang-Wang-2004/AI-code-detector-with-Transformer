class C1(object):

    def __init__(self):
        self.__vals = [20, 50, 100, 200, 500]
        self.__cnt = [0] * len(self.__vals)

    def deposit(self, a1):
        """
        """
        for v1, v2 in enumerate(a1):
            self.__cnt[v1] += v2

    def withdraw(self, a1):
        """
        """
        v1 = [0] * len(self.__cnt)
        for v2 in reversed(range(len(self.__vals))):
            v1[v2] = min(a1 // self.__vals[v2], self.__cnt[v2])
            a1 -= v1[v2] * self.__vals[v2]
        if a1:
            return [-1]
        for v2, v4 in enumerate(v1):
            self.__cnt[v2] -= v4
        return v1
