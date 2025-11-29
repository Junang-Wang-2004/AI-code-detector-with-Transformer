import bisect

class C1(object):

    def __init__(self):
        self.__times = []
        self.__prefix = [0]

    def record(self, a1, a2):
        """
        """
        self.__times.append(a1)
        self.__prefix.append(self.__prefix[-1] + a2)

    def totalScore(self, a1, a2):
        """
        """
        v1 = bisect.bisect_left(self.__times, a1)
        v2 = bisect.bisect_right(self.__times, a2) - 1
        return self.__prefix[v2 + 1] - self.__prefix[v1]
