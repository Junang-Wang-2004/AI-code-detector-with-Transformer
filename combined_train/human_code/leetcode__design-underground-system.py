import collections

class C1(object):

    def __init__(self):
        self.__live = {}
        self.__statistics = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, a1, a2, a3):
        """
        """
        self.__live[a1] = (a2, a3)

    def checkOut(self, a1, a2, a3):
        """
        """
        v1, v2 = self.__live.pop(a1)
        self.__statistics[v1, a2][0] += a3 - v2
        self.__statistics[v1, a2][1] += 1

    def getAverageTime(self, a1, a2):
        """
        """
        v1, v2 = self.__statistics[a1, a2]
        return float(v1) / v2
