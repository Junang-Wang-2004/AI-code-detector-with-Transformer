import bisect

class C1(object):

    def __init__(self):
        self.__records = collections.defaultdict(list)
        self.__lookup = {'minute': 60, 'hour': 3600, 'day': 86400}

    def recordTweet(self, a1, a2):
        """
        """
        bisect.insort(self.__records[a1], a2)

    def getTweetCountsPerFrequency(self, a1, a2, a3, a4):
        """
        """
        v1 = self.__lookup[a1]
        v2 = a3
        v3 = []
        while v2 <= a4:
            v4 = min(v2 + v1, a4 + 1)
            v3.append(bisect.bisect_left(self.__records[a2], v4) - bisect.bisect_left(self.__records[a2], v2))
            v2 += v1
        return v3
