# Time:  O(1)
# Space: O(n)
class Fancy2(object):

    def __init__(self):
        self.__arr = []
        self.__op = [1, 0]

    def append(self, val):
        """
        """
        self.__arr.append((val-self.__op[1])*pow(self.__op[0], MOD-2, MOD)%MOD)  # O(logMOD), we treat it as O(1) here

    def addAll(self, inc):
        """
        """
        self.__op[1] = (self.__op[1]+inc) % MOD

    def multAll(self, m):
        """
        """
        self.__op = [(self.__op[0]*m) % MOD, (self.__op[1]*m) % MOD]

    def getIndex(self, idx):
        """
        """
        if idx >= len(self.__arr):
            return -1
        a, b = self.__op
        return (self.__arr[idx]*a + b) % MOD
